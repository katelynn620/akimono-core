# ������w������ 2005/03/30 �R��

$NOITEM=1;
$NOMENU=1;
Lock();
DataRead();
CheckUserPass();
OutError("�̎傪���Ȃ��̂ő������x���@�\���Ă��܂���") if !defined($id2idx{$STATE->{leader}});
RequireFile('inc-manor.cgi');

	# �����ݒ���擾
	my $id=$id2idx{$STATE->{leader}};
	ReadDTSub($DT[$id],"lord");
	my $MANORLORD=$DT[$id]->{_lord};

	ReadDTSub($DT,"seed");

my $usetime=10*60;
$i=int($Q{it});

my @MYMANOR=@{$MANOR[$i]};
$price=$MANORLORD->{"price$i"};
OutError("bad request") if !$price;

$stock=$MANORLORD->{"count$i"};
OutError("�̔��݌ɂ��s���Ă��܂�") if ($stock < 1);

$num=CheckCount($Q{num1},$Q{num2},0,$tlimit - $DT->{_seed}->{"base$i"});
$num=$stock if ($num > $stock);
OutError('���ʂ��w�肵�Ă��������B') if !$num;

$num=int($DT->{money}/$price) if $DT->{money}<$num*$price;
$num=0 if $num<0;

OutError('��₩���ł����H') if !$num;
UseTime($usetime);

$DT->{_seed}->{"base$i"}+=$num;
$DT->{_seed}->{"time$i"}=$NOW_TIME + $ripetime;
$DT->{money}-=$num*$price;
$DT->{paytoday}+=$num*$price;
OutError("�w�����鎑��������܂���") if ($DT->{money} < 0);

$MANORLORD->{"count$i"}-=$num;
$STATE->{money}+=$num*$price;
$STATE->{in}+=$num*$price;

my $ret="�����ɂ�".$MYMANOR[0]."��".$num.'��@'.GetMoneyString($price)."(�v".GetMoneyString($price*$num).")�ɂčw��".
        "/".GetTime2HMS($usetime)."����";
PushLog(0,$DT->{id},$ret);

$disp.=$ret;

	WriteDTSub($DT[$id],"lord");
	WriteDTSub($DT,"seed");
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
OutSkin();
1;
