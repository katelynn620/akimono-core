use utf8;
# 領主施政 2005/01/06 由來

$image[0]=GetTagImgKao(l("大臣"),"minister");
DataRead();
CheckUserPass();
OutError(l('政治を行えるのは領主のみです')) if $STATE->{leader}!=$DT->{id};

my $shoplist="";
my $taxsum=0;
foreach (@DT) {
$shoplist.="<OPTION VALUE=\"$_->{id}\">$_->{shopname}";
$taxsum+=$_->{taxtoday};
}

my $now=$DTlasttime+$TZ_JST-$DATE_REVISE_TIME;
my $ii=($now % $ONE_DAY_TIME);
$ii=1 if $ii < 1;
$taxsum=GetMoneyString(int($taxsum * $ONE_DAY_TIME / $ii / 10000) * 10000);

$disp.="<BIG>●".l('政務室')."</BIG><br><br>";
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>".l('大臣')."</SPAN>：".l('これはこれは領主様。ご機嫌うるわしゅうございます。')."<br>";
$disp.=l("政治のことなど大臣にお任せくださればいいのに，ご熱心ですな。ふん。")..$TRE.$TBE;
my $money=GetMoneyString($STATE->{money}+0);
my $army=$STATE->{army} + $STATE->{robina};
my $armycost=200-int($STATE->{safety} / 100); 	# 100 - 200
my $armyc=GetMoneyString($STATE->{army} * $armycost);

$disp.=<<"HTML";
<hr width=500 noshade size=1><BIG>●${\l('内政設定')}</BIG><br><br>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="lord-s">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="inside">
$TB$TDB${\l('街資金')}$TDB${\l('税収見込み')}$TDB${\l('税率')}
$TDB${\l('開拓対策費')}$TDB${\l('治安対策費')}$TRE
$TR$TD<b>$money</b>
$TD$taxsum
$TD<INPUT TYPE=TEXT NAME=taxrate SIZE=5 VALUE="$DTTaxrate"> %<br><small>(${\l('標準')} 20%)</small>
$TD$term[0]<INPUT TYPE=TEXT NAME=devem SIZE=10 VALUE="$STATE->{devem}">$term[1]<br><small>(${\l('標準')} $term[0]5,000,000$term[1])</small>
$TD$term[0]<INPUT TYPE=TEXT NAME=safem SIZE=10 VALUE="$STATE->{safem}">$term[1]<br><small>(${\l('標準')} $term[0]5,000,000$term[1])</small>
$TRE$TBE
<br><INPUT TYPE=SUBMIT VALUE="${\l('以上の内容で決定')}">
</FORM>

<hr width=500 noshade size=1><BIG>●${\l('賞罰')}</BIG><br><br>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="lord-s">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="taxside">
<BIG>●${\l('個別税率')}</BIG>： 
<SELECT NAME=tg>$shoplist</select>
 ${\l('の税率を')}
<SELECT NAME=md><OPTION VALUE="normal">${\l('通常')}
<OPTION VALUE="free">${\l('免除')}
<OPTION VALUE="double">${\l('２倍')}
</select> ${\l('に')} <INPUT TYPE=SUBMIT VALUE="${\l('設定する')}">
</FORM>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="lord-s">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="treset">
<BIG>●${\l('税率リセット')}</BIG>： 
${\l('すべての店の税率を 通常 に')} <INPUT TYPE=SUBMIT VALUE="${\l('リセットする')}">
</FORM>
HTML

if ($DTevent{rebel})
{
$disp.="<BIG>●".l('店舗取り締まり')."</BIG>： ".l("反乱中のため実行できません");
}
elsif ($STATE->{army} < 2000)
{
$disp.="<BIG>●".l('店舗取り締まり')."</BIG>： ".l("取り締まりに必要な兵士数が足りません");
}
elsif ($STATE->{money} < 1000000)
{
$disp.="<BIG>●".l('店舗取り締まり')."</BIG>： ".l("費用が足りません");
}
else
{
$disp.=<<"STR";
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="lord-s">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="expose">
<BIG>●${\l('店舗取り締まり')}</BIG>： 
<SELECT NAME=tg>$shoplist</select>
 ${\l('を軍隊で')} 
 <INPUT TYPE=SUBMIT VALUE="${\l('取り締まる')}"> (${\l('費用')}$term[0]1,000,000$term[1])
</FORM>
STR
}

$disp.=<<"HTML";
<hr width=500 noshade size=1><BIG>●${\l('軍事設定')}</BIG><br><br>
$TB$TR$TDB${\l('現在の兵力')}
$TD<b>$army人</b><small>（${\l('正規軍')} $STATE->{army}${\l('人')}，${\l('義勇軍')} $STATE->{robina}${\l('人')}）$TRE
$TR$TDB${\l('兵力維持費')}
$TD<b>$armyc</b><small>（${\l('正規軍１人につき%1%2%3',$term[0],$armycost,$term[1])}）$TRE
$TBE
HTML

if ($STATE->{money}>0 && !$DTevent{rebel})
{
	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="lord-s">
	$USERPASSFORM
	<INPUT TYPE=hidden NAME=mode VALUE="outside">
	<BIG>●${\l('兵力増強')}</BIG>： ${\l('兵士を')} 
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	my $stock=int($STATE->{money} / 1200);
	$msg{1000}=1000;
	$msg{5000}=5000;
	$msg{10000}=10000;
	$msg{20000}=20000;
	$msg{$stock}="$stock".l("(資金最大)");
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
	<INPUT TYPE=SUBMIT VALUE="${\l('増強する')}"> @$term[0]1,200$term[1]
	</FORM>
STR
	$disp.=<<STR;
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=hidden NAME=key VALUE="lord-s">
	$USERPASSFORM
	<INPUT TYPE=hidden NAME=mode VALUE="outdel">
	<BIG>●${\l('兵力削減')}</BIG>： ${\l('兵士を')} 
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	my $army=$STATE->{army}+0;
	$msg{1000}=1000;
	$msg{5000}=5000;
	$msg{10000}=10000;
	$msg{20000}=20000;
	$msg{$army}="$army".l("(兵士最大)");
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1000,5000,10000,20000,$army))
	{
		last if $army<$cnt || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.=<<STR;
	</SELECT>
	 ${\l('人、もしくは')} 
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2> ${\l('人')}
	<INPUT TYPE=SUBMIT VALUE="${\l('解雇する')}"> @$term[0]0$term[1]
	</FORM>
STR
}

OutSkin();
1;
