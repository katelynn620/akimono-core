use utf8;
# 荘園種購入 2005/03/30 由來

$NOITEM=1;
$NOMENU=1;
DataRead();
CheckUserPass();
OutError(l('領主がいないので荘園制度が機能していません')) if !defined($id2idx{$STATE->{leader}});
RequireFile('inc-manor.cgi');

	# 荘園設定を取得
	my $i=$id2idx{$STATE->{leader}};
	ReadDTSub($DT[$i],"lord");
	$MANORLORD=$DT[$i]->{_lord};

	ReadDTSub($DT,"seed");

my $usetime=10*60;
$i=int($Q{buy});

my @MYMANOR=@{$MANOR[$i]};
$price=$MANORLORD->{"price$i"};
OutError('bad request') if !$price;

$stock=$MANORLORD->{"count$i"};
OutError(l('販売在庫が尽きています')) if !$stock;

RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>●".l('購入')."</BIG><br><br>";

$disp.=$TB.$TR.$TDB.l("商品").$TD;
$disp.=GetTagImgManor($MYMANOR[1]).$MYMANOR[0].$TRE;
$disp.=$TR.$TDB.l("価格").$TD.'@'.GetMoneyString($price).$TRE;
$disp.=$TR.$TDB.l("販売在庫数").$TD.$stock." ".l("個").$TRE;
$disp.=$TR.$TDB.l('自店保有数').$TD.($DT->{_seed}->{"base$i"} + 0)." ".l("個").$TRE;
$disp.=$TBE;
$disp.="<hr width=500 noshade size=1>";

if($DT->{_seed}->{"base$i"}>=$tlimit)
	{$disp.='<BR>'.l('これ以上購入できません').'<BR>';}
elsif($DT->{money}<$price)
	{$disp.='<BR>'.l('資金が足りません').'<BR>';}
elsif(GetStockTime($DT->{time})<$usetime)
	{$disp.='<BR>'.l('時間が足りません').'<BR>';}
else
{
	$disp.="<FORM ACTION=\"action.cgi\" $METHOD>";
	$disp.="<INPUT TYPE=HIDDEN NAME=key VALUE=\"manor-s\">";
	$disp.="$USERPASSFORM";
	$disp.="<INPUT TYPE=HIDDEN NAME=bk VALUE=\"manor\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=it VALUE=\"$i\">";
	$disp.=l('上記を')." ";
	$limit=$tlimit - $DT->{_seed}->{"base$i"};
	$money=$MAX_MONEY;
	$money=int($DT->{money}/$price) if $price;
	$msg{1}=1;
	$msg{10}=10;
	$msg{100}=100;
	$msg{1000}=1000;
	$msg{10000}=10000;
	$msg{$stock}="$stock".l('(在庫最大)');
	$msg{$limit}="$limit".l('(保有最大)');
	$msg{$money}="$money".l('(資金最大)');
	$disp.="<SELECT NAME=num1 SIZE=1>";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1,10,50,$stock,$limit,$money))
	{
		last if $stock<$cnt || $DT->{money}<$cnt*$price || $cnt>$limit || $cnt==$oldcnt;
	
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.="</SELECT> ".l('個、もしくは')." ";
	$disp.="<INPUT TYPE=TEXT NAME=num2 SIZE=5> ".l('個')." ";

	$disp.="<INPUT TYPE=SUBMIT VALUE='".l('買う')."'>";

	$disp.="<br>(".l("消費時間:%1",GetTime2HMS($usetime)).")";
	$disp.="</FORM>";
}

OutSkin();
1;
