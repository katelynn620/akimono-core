# ���� 2005/03/30 �R��

$NOITEM=1;
DataRead();
CheckUserPass();
RequireFile('inc-manor.cgi');

$disp.="<BIG>���̎���</BIG><br><br>";

my $MANORLORD;

if (defined($id2idx{$STATE->{leader}}))
	{
	my $i=$id2idx{$STATE->{leader}};
	$disp.=$TB.$TR.$TD.GetTagImgKao($DT[$i]->{name},$DT[$i]->{icon});
	$disp.=$TD."<SPAN>�̎�</SPAN> �F <b>".$DT[$i]->{name}."</b>";
	$disp.=DignityDefine($DT[$i]->{dignity})." <small>�i".$DT[$i]->{shopname}."�j</small><br>";
	$disp.=">> ".$DT[$i]->{comment};
	$disp.=$TRE.$TBE;

	# �����ݒ���擾
	ReadDTSub($DT[$i],"lord");
	$MANORLORD=$DT[$i]->{_lord};
	}
	else
	{
$disp.=$TB.$TR.$TD.GetTagImgKao($BAL_NAME,"bal");
$disp.=$TD."�̎� �F <b>$BAL_NAME</b> <small>�i$BAL_JOB�j</small><br>";
$disp.=">> �����H ��Ȃ���m�邩�B������͂��́I";
$disp.=$TRE.$TBE;
	}

	ReadDTSub($DT,"seed");
	my $seedlock=0;
	my $ripeflag=0;

$disp.="<br><BIG>��������</BIG><br><br>";
$disp.=$TB.$TR;
$disp.=$TDB."��".$TDB."�̔��݌�".$TDB."�̔����i".$TDB."���X�ۗL".$TD.$TDB."���n��".$TDB."���承�i".$TDB."���X�ۗL".$TRE;

foreach my $i(0..$#MANOR)
	{
	my @MYMANOR=@{$MANOR[$i]};
	if ($DT->{_seed}->{"base$i"} && $DT->{_seed}->{"time$i"} < $NOW_TIME)
		{
		#���n
		$DT->{_seed}->{"ripe$i"}+=$DT->{_seed}->{"base$i"};
		delete $DT->{_seed}->{"base$i"};
		delete $DT->{_seed}->{"time$i"};
		$seedlock++;
		}
	$disp.=$TR.$TD;
	$disp.=($MANORLORD->{"count$i"}) ? "<a href=\"action.cgi?key=manor-m&$USERPASSURL&buy=".$i."&bk=manor\">" : "<b>";
	$disp.=GetTagImgManor($MYMANOR[1]).$MYMANOR[0];
	$disp.=($MANORLORD->{"count$i"}) ? "</a>" : "</b>";
	$disp.=$TD.($MANORLORD->{"count$i"} + 0)." ��";
	$disp.=$TD."@".GetMoneyString($MANORLORD->{"price$i"});
	$disp.=$TD.($DT->{_seed}->{"base$i"} + 0)." ��";
	$disp.=$TD."��".$TD.GetTagImgManor($MYMANOR[3]).$MYMANOR[2];
	$disp.=$TD."@".GetMoneyString($MANORLORD->{"cost$i"});
	$disp.=$TD.($DT->{_seed}->{"ripe$i"} + 0)." ��".$TRE;
	$ripeflag+=$DT->{_seed}->{"ripe$i"};
	}
$disp.=$TBE;

if ($ripeflag)
	{
$disp.=<<"HTML";
	<br>
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="manor-r">
	<INPUT TYPE=HIDDEN NAME=bk VALUE="manor">
	$USERPASSFORM
<BIG>�����n�����p</BIG>�F ���n����̎�̑����� 
<INPUT TYPE=SUBMIT VALUE="��������Ă��炤">
	</FORM>
HTML
	}

if ($seedlock)
	{
	Lock();		#���l�͓����t�@�C���ɃA�N�Z�X���Ȃ��̂Ń��b�N�͒x���Ă���
	WriteDTSub($DT,"seed");
	DataCommitOrAbort();
	UnLock();
	}

if ($STATE->{leader}==$DT->{id})
	{
	$disp.=<<STR;
	<br>
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="manor-f">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=form VALUE="plus">
	<INPUT TYPE=SUBMIT VALUE='�������Ǘ�����'>
	</FORM>
STR
	}

OutSkin();
1;

