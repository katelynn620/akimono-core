# use �v���O�C�� 2004/02/28 �R��

sub GetUseItemList
{
	return GetUseItemListSub(@item::USE);
}

sub GetUseItemListSub
{
	my(@USE)=@_;
	foreach my $USE (@USE)
	{
		my $ret=CheckUseItem($USE);
		$USE->{dispok}=1 if $ret==2;
		$USE->{useok}=1 if $ret==1;
	}
	return @USE;
}

sub CheckUseItem
{
	my($USE)=@_;
	my $jobfunc="item::_job_use_$USE->{no}_$DT->{job}_";
	if (defined &$jobfunc)
	{
	&$jobfunc($USE->{no});
	}
	else
	{
	$jobfunc="item::_job_use_0_$DT->{job}_";
	&$jobfunc($USE->{no}) if defined &$jobfunc;
	}
	
	my $funcbefore=$USE->{functionbefore};
	if($funcbefore)
	{
		my $ret=&{"item::".$funcbefore}($USE);
		return 2 if $ret==2;
		return 0 if $ret==1;
	}
	foreach my $item (@{$USE->{use}})
	{
		return 0 if $DT->{item}[$item->{no}-1]<$item->{count};
	}
	return 1;
}

sub GetUseItem
{
	my($no)=@_;

	foreach my $USE(@item::USE)
	{
		next if $USE->{no}!=$no;
		my $ret=CheckUseItem($USE);
		$USE->{dispok}=1 if $ret==2;
		$USE->{useok}=1 if $ret==1;
		return $USE;
	}
	return 0;
}

sub UseItem
{
	my($USE,$count)=@_;
	my $usetime=GetItemUseTime($USE);
	
	#�n���x�s���ō�ƕs�\���ǂ����𔻒�(�s�\�Ȃ�count=0)
	$count=0 if $DT->{exp}{$USE->{itemno}}<$USE->{needexp};
	
	#�K�v�E��
	$count=0 if ($USE->{needjob} && ($DT->{job} ne $USE->{needjob}));
	
	#�K�v�_��
	$count=0 if ($USE->{needpoint} && ($DT->{point} < $USE->{needpoint}));
	
	#�K�v�l�C
	$count=0 if ($USE->{needpop} && ($DT->{rank} < $USE->{needpop}));
	
	#�K�v�C�x���g
	$count=0 if ($USE->{needevent} && !$DTevent{$USE->{needevent}});
	
	#��p�s����count��␳  ���[�����Z������B
	$count=int($DT->{money}/$USE->{money}) if ($DT->{money}<$USE->{money}*$count)&&($USE->{money});
	
	#���ԕs����count��␳
	$count=int(($NOW_TIME-$DT->{time})/$usetime) if ($DT->{time}+$usetime* $count)>$NOW_TIME;
	
	#�ޗ��s����count��␳
	foreach my $item (@{$USE->{use}})
	{
		my $itemno=$item->{no};
		my $itemcount=$item->{count}*($item->{proba}==0 ? 1 : $count);
	
		if($DT->{item}[$itemno-1]<$itemcount)
		{
			$count=int($DT->{item}[$itemno-1]/$item->{count});
		}
	}
	
	#count�m��
	$USE->{result}->{count}=$count;
	return if !$count; #count��0�Ȃ玸�s
	
	#���ʗp�ϐ�������
	$USE->{result}->{useitem}=[];
	$USE->{result}->{additem}=[];
	
	#���ԂƂ�������
	UseTime($usetime*$count);
	$DT->{money}-=$USE->{money}*$count;
	$DT->{paytoday}+=$USE->{money}*$count;
	
	#�A�C�e������
	foreach my $item (@{$USE->{use}})
	{
		my $itemno=$item->{no};
		my $itemcount=MakeAmount($item->{count}*$count,$item->{proba});
		if($itemcount)
		{
			$DT->{item}[$itemno-1]-=$itemcount;
			push(@{$USE->{result}->{useitem}},[$itemno,$itemcount]);
			push(@{$USE->{result}->{usemsg}},$item->{message});
		}
	}
	
	#�A�C�e���擾
	foreach my $item (@{$USE->{result}->{create}})
	{
		my $itemno=$item->{no};
		my $itemcount=MakeAmount($item->{count}*$count,$item->{proba});
		if($itemcount)
		{
			if($itemcount+$DT->{item}[$itemno-1]>$ITEM[$itemno]->{limit})
			{
				$itemcount-=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1];
				my $trashitem="����ȏ㎝�ĂȂ��̂�".$ITEM[$itemno]->{name}."��".($itemcount).$ITEM[$itemno]->{scale}."�j�����܂���";
				$DTwholestore[$itemno-1]+=$itemcount;
				push(@{$USE->{result}->{trashmsg}},$trashitem);
				$itemcount=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1];
			}
			$DT->{item}[$itemno-1]+=$itemcount;
			push(@{$USE->{result}->{additem}},[$itemno,$itemcount]);
			push(@{$USE->{result}->{addmsg}},$item->{message});
		}
	}
	
	#�s��݌Ƀ`�F�b�N���␳
	CheckWholeStore();
	
	#�A�C�e���ʊ֐����݃`�F�b�N
	RequireFile('inc-item.cgi');
	my $itemfunc="item::".$USE->{result}->{function};
	$itemfunc="" if !defined(&$itemfunc);
	
	#�A�C�e���ʊ֐��Ăяo��
	if($itemfunc ne '')
	{
		#�ϐ��A�N�Z�X�ȕ։�
		@item::DT=@DT;
		$item::DTS=$DT[$USE->{arg}->{targetidx}]; #target�X
		$item::count=$USE->{result}->{count};
		$item::USE=$USE;
		$item::DT=$DT;
		@item::ITEM=@ITEM;
		
		$USE->{result}->{function_return}=&$itemfunc();
	}

	#�n���x����
	if($USE->{exp})
	{
		#�n���x�v���X
		my $exp=$DT->{exp}->{$USE->{itemno}};
		$USE->{result}->{expold}=$exp+0;
		my $expplus=$USE->{exp}*$USE->{result}->{count};
		$expplus=1000-$exp if $exp+$expplus>1000;
		$DT->{exp}->{$USE->{itemno}}+=$expplus;
		
		#�n���x���v�l�`�F�b�N
		my $expsum=0;
		foreach(values(%{$DT->{exp}}))
		{
			$expsum+=$_;
		}
		#�n���x�I�[�o�[������
		if($LIMIT_EXP>0 && $expsum>$LIMIT_EXP)
		{
			$expsum-=$LIMIT_EXP;
			
			my @key=sort { $DT->{exp}{$a} <=> $DT->{exp}{$b} }keys(%{$DT->{exp}});
			my $keycnt=$#key;
			foreach(@key)
			{
				next if $_==$USE->{itemno};
				my $expdown=int($expsum/$keycnt);
				$expdown=$DT->{exp}{$_} if $DT->{exp}{$_}<$expdown;
				$DT->{exp}{$_}-=$expdown;
				delete $DT->{exp}{$_} if !$DT->{exp}{$_};
				$expsum-=$expdown;
				$keycnt--;
			}
		}
	}
}

sub MakeAmount
{
	my($cnt,$p)=@_;
	return 0 if ($p <= 0);
	return $cnt if ($p >= 1000);
	if ($cnt < 20) {
		my $i=0;
		foreach(1..$cnt) { $i++ if rand(1000)<$p; }
		return $i;
		}
	# ���K����
	$p = ($p / 1000);
	my $ave=$cnt*$p;
	my $sigma=$ave*(1-$p);
	my $t = (-2*$sigma*rand())*(sin(2*3.1415926535*rand()));
	return int( sqrt(($t < 0) ? -$t : $t)+$ave +0.5);
}

sub AddItem
{
	my($DT,$itemno,$count)=@_;
	
	$count=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$count>$ITEM[$itemno]->{limit};

	$DT->{item}[$itemno-1]+=$count;
	
	return $count;
}

sub GetBackUrl
{
	my($urltype,$page,$type)=split(/!/,$Q{bk} || $REFERER);
	return "" if $urltype eq 'none';
	
	my %url=(
		s	=>	"key=stock&$USERPASSURL",
		p	=>	"key=shop-b&$USERPASSURL&pg=$page",
		p2	=>	"key=shop-a&$USERPASSURL&pg=$page&t=2&itn=$type",
		m	=>	"key=shop-m&$USERPASSURL&pg=$page",
		sc	=>	"key=main&$USERPASSURL",
	);
	my $url=$url{$urltype}; $url||="key=$urltype&$USERPASSURL";
	
	return '<A HREF="action.cgi?'.$url.'">[�߂�]</A>';
}

1;
