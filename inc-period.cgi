# ���Z���� 2005/03/30 �R��

	foreach(keys(%GUILD))
	{
		$GUILD_DATA{$_}->{in}=0;
		$GUILD_DATA{$_}->{out}=0;
		delete($GUILD_DATA{$_}->{guild});
		unlink($COMMON_DIR."/".$_.".pl") if ($GUILD_DATA{$_}->{money} < 0);
	}
	
	if(defined($DT[0]))
	{
		#���̎��_�ł̃g�b�v�̓X��TOP�J�E���^��+1
		$DT[0]->{rankingcount}++;
		
		#�D���Ҕ��\
		my $DT=$DT[0];
		my $count=$DT->{rankingcount}==1 ? "���D��" : $DT->{rankingcount}."�x�ڂ̗D��";
		my $msg="�u�����̗D���X��".$DT->{shopname}."����ł����B".$count."���߂łƂ��������܂��v";
		PushLog(1,0,$msg);
		
		$msg="�u�_����".$DT->{point}."�_";
		$msg.="�ŁA2�ʂƂ̍���".($DT->{point}-$DT[1]->{point})."�_" if defined($DT[1]);
		$msg.="�ł����v";
		PushLog(1,0,$msg);
	}
	
	require "$ITEM_DIR/funcupdate.cgi" if $DEFINE_FUNCUPDATE;
	
	#���Z���̃h���S�����[�X���x����
	DragonBalance();

	#���Z���̃J�X�^������
	UpdateResetBefore() if defined(&UpdateResetBefore);

	#�d�Ŋz���Z�b�g�i�̎吧�j
	my $taxin=0;

	my $dtcount=0;
	foreach my $DT (@DT)
	{
		$dtcount++;
		
		#�o�c�ҕs��
		if ($NOW_TIME-$DT->{foundation} > 43200 && $DT->{blocklogin} ne 'stop')
		{
			if ($DT->{lastlogin}+$EXPIRE_TIME<$NOW_TIME)
			{
			CloseShop($DT->{id},'�o�c�ҕs��');
			PushLog(1,0,$DT->{shopname}."���o�c�ҕs�݂̂��ߕX���܂����B");
			}
		}

		#�h���S�����[�X���Z
		if ($DT->{dragon})
			{
			PushLog(0,$DT->{id},"�h���S�����[�X�̎��x ".GetMoneyString($DT->{dragon}));
			$DT->{money}+=$DT->{dragon};
			$DT->{drmoney}+=$DT->{dragon};
			$DT->{saletoday}+=$DT->{dragon} if ($DT->{dragon} > 0);
			$DT->{paytoday}-=$DT->{dragon} if ($DT->{dragon} < 0);
			}

		#�O���̏���ۑ�
		$DT->{rankingyesterday}=$dtcount;
		$DT->{profitstock}=int(($DT->{profitstock}*$PROFIT_DAY_COUNT+$DT->{saletoday}-$DT->{paytoday})/($PROFIT_DAY_COUNT+1));
		$DT->{saleyesterday}=$DT->{saletoday};
		$DT->{saletoday}=0;
		$DT->{payyesterday}=$DT->{paytoday};
		$DT->{paytoday}=0;
		$DT->{itemyesterday}=$DT->{itemtoday};
		$DT->{itemtoday}={};
		$DT->{taxyesterday}=$DT->{taxtoday};
		$DT->{taxtoday}=0;
		
		#�������I�[�o�[�`�F�b�N���s���l�C��
		foreach my $cnt (1..$MAX_ITEM)
		{
			$DT->{item}[$cnt-1]=$ITEM[$cnt]->{limit} if $DT->{item}[$cnt-1]>$ITEM[$cnt]->{limit};
			$DT->{item}[$cnt-1]=int($DT->{item}[$cnt-1]);
		}
		
		#�ێ��������
		my $cost=int($DT->{costtoday});
		$cost+=$SHOWCASE_COST[$DT->{showcasecount}-1];
		$DT->{money}-=$cost;
		$DT->{paytoday}+=$cost;
		
		#�d�Ŏ����i�̎吧�j
		$taxin+=$DT->{taxyesterday};

		#�M���h���
		if($DT->{guild} ne '')
		{
			my $money=int($DT->{saleyesterday}*$GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/1000);
			EditGuildMoney($DT->{guild},$money);
			$DT->{money}-=$money;
						# �M���h�U�h���R�ϓ�
			$GUILD_DATA{$DT->{guild}}->{atk}=int($GUILD_DATA{$DT->{guild}}->{atk} *24 /25);
			$GUILD_DATA{$DT->{guild}}->{def}=int($GUILD_DATA{$DT->{guild}}->{def} *9 /10);
			$GUILD_DATA{$DT->{guild}}->{def}+=int($money/800);
			$GUILD_DATA{$DT->{guild}}->{def}=1000 if ($GUILD_DATA{$DT->{guild}}->{def}>1000);
		}
		
		$DT->{costyesterday}=$cost;
		$DT->{costtoday}=0;
		
		#�n���x���R����
		foreach my $key (keys(%{$DT->{exp}}))
		{
			$DT->{exp}{$key}-=int($DT->{exp}{$key}*$EXP_DOWN_RATE/1000) if $EXP_DOWN_RATE;
			$DT->{exp}{$key}-=$EXP_DOWN_POINT;
			delete $DT->{exp}{$key} if $DT->{exp}{$key}<=0;
		}

		#�݈ʃ|�C���g���R����
		if ($DT->{dignity} && rand(100) < 25)
		{
			my $i=int( ($DT->{dignity}) / 12) + 1;
			$DT->{dignity}-=$i;
		}
	}
	SortDT();
	
	#�̓y�f�[�^����
	$STATE->{people}=$DTpeople;	#�O���l����ۑ��B
	$DTpeople=(24000 * $DTusercount) + 100000 + ($STATE->{develop} * 30) + ($STATE->{safety} * 20);	#�O����ԂŐl������B
	$STATE->{money}+=$taxin;
	$STATE->{in}=$taxin;
	$STATE->{develop}+=int(($STATE->{devem} / $STATE->{people} * 200) - ($STATE->{develop}/10) - rand(200));	#500���~���W���i20���l�j
	$STATE->{safety}+=int(($STATE->{safem} / $STATE->{people} * 200) - ($STATE->{safety}/10) - rand(200));	#500���~���W���i20���l�j

	if ($STATE->{army} + $STATE->{robina}< 10000)
		{
		#���m�����Ȃ��ꍇ�̃y�i���e�B
		$STATE->{safety}-=int( (10000 - $STATE->{army}- $STATE->{robina}) / 20);
		PushLog(2,0,"�X�̌�q�R�����Ȃ����߁C�������������Ă��܂��B");
		}
	$STATE->{develop}=1000 if $STATE->{develop} < 1000;
	$STATE->{safety}=1000 if $STATE->{safety} < 1000;
	my $armycost=200-int($STATE->{safety} / 100);
	$STATE->{out}=($STATE->{army}*$armycost) + $STATE->{devem} + $STATE->{safem};
	$STATE->{money}-=$STATE->{out};
	if ($DTevent{rebel})
		{
		$DTevent{rebel}=$NOW_TIME+86400*3;
		}
		else
		{
		RebelRobin();
		}
	$STATE->{army}+=$STATE->{robina};	# �`�E�R�𐳋K�R�ɁB
	if ($STATE->{money} < 0)
	{
		#�����𕥂��Ȃ�
		PushLog(2,0,"�X������������C�X�̌�q�R�ɋ������x�����Ȃ��悤�ł��B");
		$STATE->{army}=int($STATE->{army} / 3);
		$STATE->{money}=0;
	}
	if (defined($id2idx{$STATE->{leader}}))
	{
	$STATE->{robina}=0;
	}
	else
	{
	$STATE->{robina}=$STATE->{army};
	$STATE->{army}=0;
	}

	#���Z���̃J�X�^�������i���Z�b�g��j
	UpdateResetAfter() if defined(&UpdateResetAfter);
	
	#�f�[�^�o�b�N�A�b�v($BACKUP�����$BACKUP��)
	mkdir($BACKUP_DIR.$BACKUP,$DIR_PERMISSION) if !(-e $BACKUP_DIR.$BACKUP);
	rename($BACKUP_DIR.$BACKUP,$BACKUP_DIR."_work");
	foreach my $count (reverse(1..$BACKUP-1))
	{
		mkdir($BACKUP_DIR.$count,$DIR_PERMISSION) if !(-e $BACKUP_DIR.$count);
		rename($BACKUP_DIR.$count,$BACKUP_DIR.($count+1));
	}
	rename($BACKUP_DIR."_work",$BACKUP_DIR."1");
	
	foreach my $filetype (@BACKUP_FILES)
	{
		open(IN,GetPath($filetype));
		open(OUT,">".GetPath($BACKUP_DIR."1",$filetype));
		while(<IN>){print OUT $_;}
		close(OUT);
		close(IN);
	}
	
	#�����ȃZ�b�V�����f�[�^(�����؂�)���폜
	opendir(SESS,$SESSION_DIR);
	my @dir=readdir(SESS);
	closedir(SESS);
	my $sessiontimeout=$NOW_TIME-$EXPIRE_TIME;
	foreach(map{"$SESSION_DIR/$_"}grep(/^.+\.cgi$/,@dir))
	{
		unlink $_ if (stat($_))[9]<$sessiontimeout; # $EXPIRE_TIME�g���Ȃ���Ώ���
	}
	MakeGuildFile();
1;


sub RebelRobin
{
return if !defined($id2idx{$STATE->{leader}});
my $i=int(15000 - $STATE->{develop} - $STATE->{safety} - rand(2500));
my $ii=int(50000000 - $STATE->{money} - rand(5000000));
return if ($i > 1000)&&($ii > 5000000);
PushLog(2,0,"$BAL_JOB$BAL_NAME���s���ȓ����������Ă��܂��B"),return if ($i > 0) && ($ii > 0);
if (rand(100) < 30)
	{
	$DTevent{rebel}=$NOW_TIME+86400*3;
	$STATE->{robinb}=10000;
	PushLog(2,0,"$BAL_JOB$BAL_NAME���X�ɍU�ߍ��݁C�������N�����܂����I");
	}
	else
	{
	PushLog(2,0,"$BAL_JOB$BAL_NAME���U�߂鎞�@�����������Ă���悤�ł��B");
	}
}

sub DragonBalance
{
	my $fn=GetPath($COMMON_DIR,"drapay-".$MYDIR);
	open(IN,$fn) or return;
	my @req=<IN>;
	close(IN);
	foreach (0..$#req)
		{
		chop $req[$_];
		my @buf=split(/\t/,$req[$_]);
		next if !defined($id2idx{$buf[0]});
		my $i=$id2idx{$buf[0]};
		$DT[$i]->{dragon}+=$buf[1];
		}
	unlink $fn;
}

