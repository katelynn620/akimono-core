use utf8;
# 荘園種購入処理 2005/03/30 由來

$NOITEM=1;
$NOMENU=1;
Lock();
DataRead();
CheckUserPass();
OutError(l('領主がいないので荘園制度が機能していません')) if !defined($id2idx{$STATE->{leader}});
RequireFile('inc-manor.cgi');

	# 荘園設定を取得
	my $id=$id2idx{$STATE->{leader}};
	ReadDTSub($DT[$id],"lord");
	my $MANORLORD=$DT[$id]->{_lord};

	ReadDTSub($DT,"seed");

my $usetime=10*60;
$i=int($Q{it});

my @MYMANOR=@{$MANOR[$i]};
$price=$MANORLORD->{"price$i"};
OutError('bad request') if !$price;

$stock=$MANORLORD->{"count$i"};
OutError(l('販売在庫が尽きています')) if ($stock < 1);

$num=CheckCount($Q{num1},$Q{num2},0,$tlimit - $DT->{_seed}->{"base$i"});
$num=$stock if ($num > $stock);
OutError(l('数量を指定してください。')) if !$num;

$num=int($DT->{money}/$price) if $DT->{money}<$num*$price;
$num=0 if $num<0;

OutError(l('冷やかしですか？')) if !$num;
UseTime($usetime);

$DT->{_seed}->{"base$i"}+=$num;
$DT->{_seed}->{"time$i"}=$NOW_TIME + $ripetime;
$DT->{money}-=$num*$price;
$DT->{paytoday}+=$num*$price;
OutError(l('購入する資金がありません')) if ($DT->{money} < 0);

$MANORLORD->{"count$i"}-=$num;
$STATE->{money}+=$num*$price;
$STATE->{in}+=$num*$price;

my $ret = l(
    "荘園にて%1を%2個@%3(計%4)にて購入/%5消費",
    $MYMANOR[0],
    $num,
    GetMoneyString($price),
    GetMoneyString( $price * $num ),
    GetTime2HMS($usetime)
);
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
