# ������w�� 2005/03/30 �R��

$NOITEM=1;
$NOMENU=1;
DataRead();
CheckUserPass();
OutError("�̎傪���Ȃ��̂ő������x���@�\���Ă��܂���") if !defined($id2idx{$STATE->{leader}});
RequireFile('inc-manor.cgi');

	# �����ݒ���擾
	my $i=$id2idx{$STATE->{leader}};
	ReadDTSub($DT[$i],"lord");
	$MANORLORD=$DT[$i]->{_lord};

	ReadDTSub($DT,"seed");

my $usetime=10*60;
$i=int($Q{buy});

my @MYMANOR=@{$MANOR[$i]};
$price=$MANORLORD->{"price$i"};
OutError("bad request") if !$price;

$stock=$MANORLORD->{"count$i"};
OutError("�̔��݌ɂ��s���Ă��܂�") if !$stock;

RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>���w��</BIG><br><br>";

$disp.=$TB.$TR.$TDB."���i".$TD;
$disp.=GetTagImgManor($MYMANOR[1]).$MYMANOR[0].$TRE;
$disp.=$TR.$TDB."���i".$TD.'@'.GetMoneyString($price).$TRE;
$disp.=$TR.$TDB."�̔��݌ɐ�".$TD.$stock." ��".$TRE;
$disp.=$TR.$TDB.'���X�ۗL��'.$TD.($DT->{_seed}->{"base$i"} + 0)." ��".$TRE;
$disp.=$TBE;
$disp.="<hr width=500 noshade size=1>";

if($DT->{_seed}->{"base$i"}>=$tlimit)
	{$disp.='<BR>����ȏ�w���ł��܂���<BR>';}
elsif($DT->{money}<$price)
	{$disp.='<BR>����������܂���<BR>';}
elsif(GetStockTime($DT->{time})<$usetime)
	{$disp.='<BR>���Ԃ�����܂���<BR>';}
else
{
	$disp.="<FORM ACTION=\"action.cgi\" $METHOD>";
	$disp.="<INPUT TYPE=HIDDEN NAME=key VALUE=\"manor-s\">";
	$disp.="$USERPASSFORM";
	$disp.="<INPUT TYPE=HIDDEN NAME=bk VALUE=\"manor\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=it VALUE=\"$i\">";
	$disp.="��L�� ";
	$limit=$tlimit - $DT->{_seed}->{"base$i"};
	$money=$MAX_MONEY;
	$money=int($DT->{money}/$price) if $price;
	$msg{1}=1;
	$msg{10}=10;
	$msg{100}=100;
	$msg{1000}=1000;
	$msg{10000}=10000;
	$msg{$stock}="$stock(�݌ɍő�)";
	$msg{$limit}="$limit(�ۗL�ő�)";
	$msg{$money}="$money(�����ő�)";
	$disp.="<SELECT NAME=num1 SIZE=1>";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1,10,50,$stock,$limit,$money))
	{
		last if $stock<$cnt || $DT->{money}<$cnt*$price || $cnt>$limit || $cnt==$oldcnt;
	
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.="</SELECT> �A�������� ";
	$disp.="<INPUT TYPE=TEXT NAME=num2 SIZE=5> �� ";

	$disp.="<INPUT TYPE=SUBMIT VALUE='����'>";

	$disp.="<br>(�����:".GetTime2HMS($usetime).")";
	$disp.="</FORM>";
}

OutSkin();
1;
