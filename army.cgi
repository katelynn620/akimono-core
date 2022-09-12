use utf8;
# 兵士駐屯所 2005/01/06 由來

$image[0]=GetTagImgKao("案内人","army");
DataRead();
CheckUserPass();
ReadArmy();
RequireFile('inc-html-ownerinfo.cgi');

my $price=($DTevent{rebel}) ? 1500 : 1000;
my $level=DignityDefine($DT->{dignity},2);
$level=$DIGNITY[0] if !$level;

$disp.="<BIG>●".l('傭兵所')."</BIG><br><br>";
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>".l('案内人')."</SPAN>：".l('ここにはドワーフ兵たちが雇い手を求めて集まっています。')."<br>";
$disp.=l("彼らを集めて反乱を起こすも，逆に領主を守るも，雇い主次第です。").$TRE.$TBE;

$disp.="<hr width=500 noshade size=1><BIG>●".l('%1の雇用状況',$DT->{shopname})."</BIG><br><br>";
$disp.="$TB$TR$TDB".l('爵位')."$TD$level <small>(".l('経験値')." ".($DT->{dignity}+0)."pt)$TRE";
$disp.="$TR$TDB".l('雇用最大数')."$TD".(($DT->{dignity}+0)*1000).l('人')."$TRE";
$disp.="$TR$TDB".l('雇用費用')."$TD@".GetMoneyString($price)."$TRE";
$disp.="$TR$TDB".l('雇用数')."$TD".($ARMY{$DT->{id}}+0)."人$TRE";
$disp.="$TR$TDB".l('状態')."$TD".($RIOT{$DT->{id}} ? "<SPAN>".l('反乱')."</SPAN>" : l("待機")).$TRE;
$disp.=$TBE;

ArmyBuy();
if ($ARMY{$DT->{id}})
	{
	ArmyFire();
	ArmyRebel() if !$DTevent{rebel};
	ArmyAction() if $DTevent{rebel} && !$RIOT{$DT->{id}};
	}
OutSkin();
1;


sub ArmyBuy
{
my $usetime=60*40;
my $limit= ($DT->{dignity}+0)*1000 - $ARMY{$DT->{id}};
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>●'.l('兵士雇用').'</BIG>：'.l('兵士を雇うには爵位を上げる必要があります').'<BR>',return if $limit <= 0;
$disp.='<BIG>●'.l('兵士雇用').'</BIG>：'.l('資金が足りません').'<BR>',return if $DT->{money}<$price;
$disp.='<BIG>●'.l('兵士雇用').'</BIG>：'.l('時間が足りません').'<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="plus">
	<BIG>●${\l('兵士雇用')}</BIG>： ${\l('兵士を')} 
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	$money=int($DT->{money}/$price);
	$msg{1000}=1000;
	$msg{5000}=5000;
	$msg{10000}=10000;
	$msg{20000}=20000;
	$msg{$limit}="$limit(".l('雇用最大').")";
	$msg{$money}="$money(".l('資金最大').")";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1000,5000,10000,20000,$limit,$money))
	{
		last if $cnt>$money || $cnt>$limit || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.=<<STR;
	</SELECT>
	 ${\l('人、もしくは')} 
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2> ${\l('人')}
	<INPUT TYPE=SUBMIT VALUE="${\l('雇用する')}">
STR
	$disp.="(".l('消費時間').":".GetTime2HMS($usetime).")</FORM>";
}


sub ArmyFire
{
my $usetime=60*10;
my $stock=($ARMY{$DT->{id}}+0);
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>●'.l('兵士解雇').'</BIG>：'.l('時間が足りません').'<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="fire">
	<BIG>●${\l('兵士解雇')}</BIG>： ${\l('兵士を')} 
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	$msg{1000}=1000;
	$msg{5000}=5000;
	$msg{10000}=10000;
	$msg{20000}=20000;
	$msg{$stock}="$stock(".l('兵士最大').")";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1000,5000,10000,20000,$stock))
	{
		last if $stock<$cnt || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.=<<STR;
	</SELECT>
	 ${\l('人、もしくは')} 
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2> ${\l('人')}
	<INPUT TYPE=SUBMIT VALUE="${\l('解雇する')}">
STR
	$disp.="(".l('消費時間').":".GetTime2HMS($usetime).")</FORM>";
}


sub ArmyRebel
{
return if ($STATE->{leader}==$DT->{id});
my $usetime=60*30;
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>●'.l('武装蜂起').'</BIG>：'.l('反乱に必要な兵士数が足りません。').'<BR>',return if ($ARMY{$DT->{id}} < 2500);
$disp.='<BIG>●'.l('武装蜂起').'</BIG>：'.l('時間が足りません').'<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="rebelon">
	<BIG>●${\l('武装蜂起')}</BIG>： 
	<INPUT TYPE=TEXT NAME=cmd SIZE=10 VALUE="">
	(${\l('rebel と入力')})
	${\l('反乱を')} <INPUT TYPE=SUBMIT VALUE="${\l('開始する')}">
STR
	$disp.="(".l('消費時間').":".GetTime2HMS($usetime).")</FORM>";
}


sub ArmyAction
{
my $usetime=60*20;
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>●'.l('反乱加勢').'</BIG>：'.l('時間が足りません').'<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="rside">
	<BIG>●${\l('反乱加勢')}</BIG>： 
	<INPUT TYPE=TEXT NAME=cmd SIZE=10 VALUE="">
	(${\l('rebel と入力')})
	${\l('反乱に')} <INPUT TYPE=SUBMIT VALUE="${\l('呼応する')}">
STR
	$disp.="(".l('消費時間').":".GetTime2HMS($usetime).")</FORM>";

$usetime=60*20;
$disp.="<hr width=500 noshade size=1>";
$disp.='<BIG>●'.l('護衛協力').'</BIG>：'.l('時間が足りません').'<BR>',return if GetStockTime($DT->{time})<$usetime;

	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="army-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=bk VALUE="army">
	<INPUT TYPE=hidden NAME=mode VALUE="lside">
	<BIG>●${\l('護衛協力')}</BIG>： 
	${\l('兵士を領主の護衛軍に')} <INPUT TYPE=SUBMIT VALUE="${\l('派遣する')}">
STR
	$disp.="(".l('消費時間').":".GetTime2HMS($usetime).")</FORM>";
}
