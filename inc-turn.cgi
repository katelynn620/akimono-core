# �^�[������ 2004/02/28 �R��

require (GetPath($ITEM_DIR,"event"));

Lock();
DataRead();
ReadGuild();
ReadGuildData();
$now=$NOW_TIME+$TZ_JST-$DATE_REVISE_TIME;
$lasttime=$DTlasttime+$TZ_JST-$DATE_REVISE_TIME;

$temptimenow=$DTlasttime;

	#1span���Ƃɏ������J��Ԃ����߂̏���
	undef @timespan;
	while(int($lasttime/$ONE_DAY_TIME)<int($now/$ONE_DAY_TIME))
	{
		push(@timespan,[1,$ONE_DAY_TIME-($lasttime%$ONE_DAY_TIME)]);
		$lasttime+=$ONE_DAY_TIME-($lasttime%$ONE_DAY_TIME);
	}
	push(@timespan,[0,$now-$lasttime]);
	$lasttime+=$now-$lasttime;

	$DTlasttime=$lasttime-$TZ_JST+$DATE_REVISE_TIME;
	$now=$now-$TZ_JST+$DATE_REVISE_TIME;
	OutError("error:$DTlasttime,$now,".(($DTlasttime-$now)/60)."<HR>$disp") if $DTlasttime!=$now;
	
	#�����J�n
	foreach $TM (@timespan)
	{
		my $dateupdate=$TM->[0];
		my $timespan=$TM->[1];
		
		$TIMESPAN=$timespan;
		
		next if $timespan<=0; # -1�����邱�Ƃ��m�F�����̂ŁB�������킩��Ȃ��̂ł����őΉ��B
		
		#�X�܁E���i�ʗ��q���v�Z����
		my $itemranksum=0;
		foreach my $ITEM (@ITEM)
			{$itemranksum+=$ITEM->{popular};}
		
		my $dtranksum=0;
		foreach my $DT (@DT)
		{
			my $group=-1;
			foreach my $cnt(0..$DT->{showcasecount}-1)
			{
				# ���X����
				my $itemno=$DT->{showcase}[$cnt];
				if($itemno && ($group!=-1 && $group!=$ITEM[$itemno]->{type}))
					{$group=-1; last}
				$group=$ITEM[$itemno]->{type} if $itemno;

				#�A�C�e���ʍw���l���Z�o
				my $price=$DT->{price}[$cnt];
				if($itemno>0 && $price>0 && $DT->{item}[$itemno-1])
				{
					$ITEM[$itemno]->{buypeoplebase}+=($ITEM[$itemno]->{price}/$price)**($cnt==0?4:3);
				}
			}
			$DT->{temprank}=$DT->{rank};
			if($group!=-1){$DT->{temprank}+=1000;}
			$dtranksum+=$DT->{temprank};
		}
		
		foreach $cnt (1..$MAX_ITEM)
		{
			next if !$ITEM[$cnt]->{popular};
			my $ITEM=$ITEM[$cnt];
			$ITEM->{buypeople}=$DTpeople*$SALE_SPEED/$ITEM->{popular}*$timespan/86400;
		}
		
		# ���v/�����o�����X�擾
		GetMarketStatus();
		
		#�X�ܕʔ��㏈�����[�v
		my $salesumall=0;
		my $nowranking=0;
		my $peopleup=0;
		my $peopledown=0;
		my $peopleupsalerate=($DTpeople/100000)**2;	#���Ƃ���1.5
		foreach my $DT (@DT)
		{
			$nowranking++;
			
			my $rankdown=0;
			my $rankup=0;
			my $salesum=0;
			
			my %showcaseitemno=();
			
			$DT->{_sale_count_}={}; # @@item funcs ��Ɨp
			
			foreach $cnt (0..$DT->{showcasecount}-1)
			{
				$itemno=$DT->{showcase}[$cnt];
				if($itemno && $DT->{item}[$itemno-1])
				{
					#�ێ���v�Z�p�f�[�^�Z�b�g
					$showcaseitemno{$itemno}++;
					
					#�w���q���v�Z
					$rank=$DT->{temprank};
					$rank=99 if $rank<100;
					my $ichioshi=$cnt==0 ? 4:3;
					my $buypeopletemp=$ITEM[$itemno]->{buypeople}
						*(($ITEM[$itemno]->{price}/$DT->{price}[$cnt])**($cnt==0?4:3))
						/($ITEM[$itemno]->{buypeoplebase}+1);
					$buypeople=$rank / ($dtranksum/($#DT+1)) * $buypeopletemp;
					
					#���㐔����
					my $sale=0;
					$rank=($ITEM[$itemno]->{price}/$DT->{price}[$cnt]);
					$rank/=($DT->{price}[$cnt]-$ITEM[$itemno]->{price})/10000 if $rank<1;
					if($buypeople>0)
						{$sale=$buypeople/2*0+rand($buypeople * ($rank>1?1:$rank));}
					if($sale<1 && $sale>0)
						{if(rand(1/$sale)<1){$sale=1;}}
					$sale=int($sale);
					
					#���㐔1�ȏ�̏ꍇ�̏���
					if($sale>0)
					{
						my $itembox=\$DT->{item}[$itemno-1];
						#�������ŕ␳
						if($sale>$$itembox){$sale=$$itembox;}
						
						#�l�CUP/DOWN
						my $rankupmulti=((10-($DT->{rank}/1000))**2)/5;
						#���v�����o�����X���l�CUP
						my $pricerate=$ITEM[$itemno]->{marketprice}/$DT->{price}[$cnt];
						$pricerate=2 if $pricerate>2;
						my $rankupsale=rand($rankupmulti/$ITEM[$itemno]->{uppoint}*$ITEM[$itemno]->{point}/10*$sale*$pricerate);
						$rankupsale=$timespan/3 if $rankupsale>$timespan/3; # 5���Ԃōő�1%�㏸�̃��~�b�g����
						$rankup+=$rankupsale;
						
						#���㏈��
						my $saleprice=$sale*$DT->{price}[$cnt];
						
						my($taxrate,$tax)=GetSaleTax($itemno,$sale,$saleprice,GetUserTaxRate($DT,$DTTaxrate));
						
						$DT->{money}+=$saleprice-$tax;	#���ڎ����ɕύX
						$DT->{trush}+=$saleprice;	#����
						$DT->{saletoday}+=$saleprice;
						$DT->{item}[$itemno-1]-=$sale;
						$DT->{itemtoday}{$itemno}+=$sale;
						$DT->{taxtoday}+=$tax;
						
						#����؂ꎞ�̐l�CDOWN
						if($DT->{item}[$itemno-1]==0)
						{
							$rankdown+=($DT->{rank}/100)**3/1000; #�l�C�ɉ����ă_�E��
						}
						
						#�l�������i�폜�j
						
						#@@item funcs ��Ɨp����
						my $_sale_count_=$DT->{_sale_count_}{$itemno}||={};
						$_sale_count_->{count}+=$sale;
						$_sale_count_->{price}+=$saleprice;
					}
					$salesum+=$sale;
					
				}
			}
			$salesumall+=$salesum;
			
			#���Ԍo�߂ɂ�閳�����l�CDOWN
			$rankdown+=sqrt($timespan)*(($DT->{rank}/1000)**$POP_DOWN_RATE)/(5**$POP_DOWN_RATE*20)*$DT->{showcasecount};
			$rankper=0.75 + ( $DT->{trush} / 10000000 );	#���݂ɂ��ϓ�
			$rankdown=$rankdown * $rankper;

			#���Ԍo�߂ɂ�閳�����l��DOWN�i�폜�j
			
			#$rankdown��$rankup�ɂ��l�CUP/DOWN����
			my $rankupdown=abs($rankup-$rankdown);
			if($rankupdown<1 && $rankdown>0)
				{if(rand(1/$rankupdown)<1){$rankupdown=1;}}
			$DT->{rank}+=int($rankup>$rankdown ? $rankupdown:-$rankupdown);
			if($DT->{rank}<0){$DT->{rank}=0;}
			if($DT->{rank}>10000){$DT->{rank}=10000;}
			
			#�ێ���v�Z���~��
			my $costsum=0;
			foreach my $idx (1..$MAX_ITEM)
			{
				next if !$DT->{item}[$idx-1];
				my $cnt=$DT->{item}[$idx-1];
				$cnt/=10 if $showcaseitemno{$idx};
				$costsum+=$ITEM[$idx]->{cost}*$cnt;
			}
			$DT->{costtoday}+=$costsum*$timespan/86400;
			$DT->{trush}+=int($costsum*$timespan/86400);	#����
		}
		#$peopledown��$peopleup�ɂ��l��UP/DOWN�����i�폜�j
		
		#@@item ��������
		@item::DT=@DT;
		$item::DT=$DT;
		@item::ITEM=@ITEM;
		$item::TIMESPAN=$TIMESPAN;
		RequireFile('inc-item.cgi');
		
		#@@item funct ����
		require "$ITEM_DIR/functurn.cgi" if $DEFINE_FUNCTURN;
		my @itemt=sort {$a->{no}<=>$b->{no}} grep($_->{functurn},@ITEM);
		foreach my $item (@itemt)
		
		{
			my $file="$ITEM_DIR/item-t/$item->{no}$FILE_EXT";
			$item::TURN_ITEMNO=$item->{no};
			$item::TURN_ITEM=$item;
			@item::TURN_DT=grep($_->{item}[$item->{no}-1],@DT);
			my $func="item::".$item->{functurn};
			my $funcexists=defined &$func;
			require $file if -e $file;
			&$func($item,@item::TURN_DT);
			undef &$func if !$funcexists;
			delete $INC{$file};
		}
		undef $item::TURN_ITEMNO;
		undef $item::TURN_ITEM;
		undef @item::TURN_DT;
		
		#@@item funcs ����
		require "$ITEM_DIR/funcsale.cgi" if $DEFINE_FUNCSALE;
		my @items=grep($_->{funcsale},@ITEM);
		foreach my $item (sort @items)
		{
			my $file="$ITEM_DIR/item-s/$item->{no}$FILE_EXT";
			$item::SALE_ITEMNO=$item->{no};
			$item::SALE_ITEM=$item;
			@item::SALE_DT=grep($_->{_sale_count_}{$item->{no}},@DT);
			next if !@item::SALE_DT;
			my $func="item::".$item->{funcsale};
			my $funcexists=defined &$func;
			require $file if -e $file;
			foreach my $DT (@item::SALE_DT)
			{
				my $_sale_count_=$DT->{_sale_count_}{$item->{no}};
				last if 'last' eq &$func($item,$DT,$_sale_count_->{count},$_sale_count_->{price});
			}
			undef &$func if !$funcexists;
			delete $INC{$file};
		}
		foreach(@DT){delete $_->{_sale_count_}} # @@item funcs ��Ɨp�폜
		undef $item::SALE_ITEMNO;
		undef $item::SALE_ITEM;
		undef @item::SALE_DT;
		
		undef $item::TIMESPAN;
		
		SortDT();
		
		#���Z����
		RequireFile('inc-period.cgi') if $dateupdate && scalar(@DT);
		
		#�s�ꏤ�i����UP/DOWN����
		foreach my $cnt (1..$MAX_ITEM)
		{
			next if !$ITEM[$cnt]->{code};
			my $ITEM=$ITEM[$cnt];
			
			#UP/DOWN����
			my $add=0;
			if($ITEM->{plus}!=0)
			{
				$add=$timespan/abs($ITEM->{plus})*$DTpeople/(100000/(($MAX_USER+$#DT-1)*0.2+1));
				# old pattern $add=$DTpeople/abs($ITEM->{plus})*$timespan/(60*60*24);
				if($add>0){$add=$add/2+rand($add/2);}else{$add=0;}
				if($add<1 && $add>0){if(rand(1/$add)<1){$add=1;}}
				$add=int($add);
				
				$DTwholestore[$cnt-1]+=$ITEM->{plus}>0 ? $add : -$add;
			}
		}
		#�s��݌ɏ�������`�F�b�N���␳
		CheckWholeStore();
		
		#�C�x���g�I������
		@event::DT=@DT;
		@event::ITEM=@ITEM;
		my %group=();
		if(defined(%DTevent))
		{
			foreach my $key (keys(%DTevent))
			{
				my $E=$EVENT{$key};
				if($DTevent{$key}<$temptimenow+$timespan)
				{
					my $msg;
					my $ret=1;
					if($E->{endfunc})
					{
						RequireFile('inc-event.cgi');
						my $extfile=GetPath($ITEM_DIR,"event-e",$key);
						require $extfile if -e $extfile;
						my $func="event::".$E->{endfunc};
						($ret,$msg)=&$func(split(/[:,]/,$E->{endfuncparam}));
						PushLog(2,0,$msg) if $msg;
						undef &$func;
					}
					if($ret)
					{
						delete $DTevent{$key};
						PushLog(2,0,$E->{endmsg}) if $E->{endmsg};
					}
					else
					{
						$group{$E->{group}}=1;
					}
				}
				else
					{$group{$E->{group}}=1;}
			}
		}
	
		#�C�x���g�J�n����
		foreach my $key (keys(%EVENT))
		{
			my $E=$EVENT{$key};
			next if $group{$E->{group}};
			
			if(rand(100000)<$timespan*$E->{startproba}/864 || $E->{startproba}==0)
			{
				my $msg;
				my $ret=1;
				if($E->{startfunc})
				{
					RequireFile('inc-event.cgi');
					my $extfile=GetPath($ITEM_DIR,"event-s",$key);
					require $extfile if -e $extfile;
					my $func="event::".$E->{startfunc};
					($ret,$msg)=&$func(split(/[:,]/,$E->{startfuncparam}));
					PushLog(2,0,$msg) if $msg;
					undef &$func;
					delete $INC{$extfile};
				}
				if($ret)
				{
					PushLog(2,0,$E->{startmsg}) if $E->{startmsg};
					$DTevent{$key}=$temptimenow+int(rand($timespan))+$E->{basetime}+int(rand($E->{plustime})) if ($E->{basetime}+$E->{plustime});
					$group{$E->{group}}=1;
				}
			}
		}
		
		foreach my $key (keys(%DTevent))
		{
			my $extfile=GetPath($ITEM_DIR,"event-n",$key);
			next if !-e $extfile;
			require $extfile;
			
			my $E=$EVENT{$key};
			my $func="event::".$E->{func};
			my($msg)=&$func(split(/[:,]/,$E->{funcparam}));
			PushLog(2,0,$msg) if $msg;
			undef &$func;
			delete $INC{$extfile};
		}
		
		$temptimenow+=$timespan;
	}
	
	#�M���h��`�t�@�C���X�V
	my $guildfilelasttime=0;
	foreach(GetGuildDirFiles())
	{
		my $file=$COMMON_DIR."/".$_.".pl";	#�g���q�ύX
		my $time=(stat($file))[9];
		$guildfilelasttime=$time if $guildfilelasttime<$time;
	}
	MakeGuildFile() if (stat(GetPath($GUILD_FILE)))[9]<$guildfilelasttime;
	
	WriteGuildData();
	DataWrite();
	RenewLog();
	DataCommitOrAbort();
	undef $TIMESPAN;
	UnLock();
1;
