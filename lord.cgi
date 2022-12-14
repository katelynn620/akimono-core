use utf8;
# 領主邸 2005/01/06 由來

DataRead();
CheckUserPass(1);
ReadArmy();

$disp.="<BIG>●".l("領主情報")."</BIG><br><br>";

# 計算部分
my %msg; $msg{free}=""; $msg{double}="";
foreach my $DT (@DT)
	{
	$msg{free}.=$DT->{shopname}."， " , next if ($DT->{taxmode}==1);
	$msg{double}.=$DT->{shopname}."， " if ($DT->{taxmode}==2);
	}

$msg{free} = substr($msg{free},0,(length($msg{free})-2)) if ($msg{free});
$msg{double} = substr($msg{double},0,(length($msg{double})-2)) if ($msg{double});


if (defined($id2idx{$STATE->{leader}}))
{
my $i=$id2idx{$STATE->{leader}};
$disp.=$TB.$TR.$TD.GetTagImgKao($DT[$i]->{name},$DT[$i]->{icon});
$disp.=$TD."<SPAN>".l("領主")."</SPAN> ： <b>".$DT[$i]->{name}."</b>";
$disp.=DignityDefine($DT[$i]->{dignity})." <small>（".$DT[$i]->{shopname}."）</small><br>";
$disp.=">> ".$DT[$i]->{comment};
$disp.=$TRE.$TBE;
}
else
{
$disp.=$TB.$TR.$TD.GetTagImgKao($BAL_NAME,"bal");
$disp.=$TD.l("領主")." ： <b>$BAL_NAME</b> <small>（$BAL_JOB）</small><br>";
$disp.=">> ".l("この街はオレの物だ。ぐわっはっは！");
$disp.=$TRE.$TBE;
}

my $armycost=200-int($STATE->{safety} / 100); 	# 100 - 200
my $purpose=l("内政重視");
if ($DTTaxrate < 20) { $purpose=l("人民解放"); }
elsif ($STATE->{army}*$armycost*2 > $STATE->{devem}+$STATE->{safem}) { $purpose=l("軍事重視"); }

$updown=l("(↑発展)");
my $peopleud=(24000 * $DTusercount) + 100000 + ($STATE->{develop} * 30) + ($STATE->{safety} * 20);
if ($DTpeople > $peopleud + 10000) { $updown=l("(↓衰退)"); }
elsif ($DTpeople > $peopleud - 10000) { $updown=l("(→停滞)"); }

$disp.="<br><BIG>●".l("内政状況")."</BIG><br><br>";
$disp.="<table width=480>".$TR;
$disp.=$TDB.l("人口").$TD.int($DTpeople/10).l("人")." <small>".$updown."</small>";
$disp.=$TDB.l("方針").$TD.$purpose.$TRE;
$disp.=$TR.$TDB.l("街資金").$TD.GetMoneyString($STATE->{money}+0);
$disp.=$TDB.l("税率").$TDNW.GetTaxMessage($DTTaxrate+0).$TRE;
$disp.=$TR.$TDB.l("前期税収").$TD.GetMoneyString($STATE->{in}+0);
$disp.=$TDB.l("前期歳出").$TD.GetMoneyString($STATE->{out}+0).$TRE;
$disp.=$TR.$TDB.l("開拓").$TDNW.GetRankMessage($STATE->{develop}+0) ;
$disp.=$TDB.l("開拓対策費").$TD.GetMoneyString($STATE->{devem}+0).$TRE;
$disp.=$TR.$TDB.l("治安").$TDNW.GetRankMessage($STATE->{safety}+0) ;
$disp.=$TDB.l("治安対策費").$TD.GetMoneyString($STATE->{safem}+0).$TRE;
$disp.=$TR.$TDB.l("免税店")."<td colspan=3><small>".$msg{free}."</small>".$TRE;
$disp.=$TR.$TDB.l("倍税店")."<td colspan=3><small>".$msg{double}."</small>".$TRE;
$disp.=$TBE;

$disp.="<br><BIG>●".l("軍事状況")."</BIG><br><br>";
$disp.=$TB.$TR;
$disp.=$TDB.l("護衛軍").$TD.GetArmyMessage($STATE->{army}+$STATE->{robina}+0,"b");
$disp.=$TDB.l("兵力維持費").$TD.GetMoneyString($STATE->{army}*$armycost).$TRE;

if ($DTevent{rebel})
{
foreach(keys(%RIOT))
	{
	next if !defined($id2idx{$_});
	$STATE->{rebel}+=$ARMY{$_};
	$DT[$id2idx{$_}]->{army}=$ARMY{$_};
	}
$STATE->{rebel}+=$STATE->{robinb};
@DTS=sort{$b->{army}<=>$a->{army}}@DT;
my $rebelid=$DTS[0]->{id};
$rebelid=$DTS[1]->{id} if ($rebelid == $STATE->{leader});
$disp.=$TR.$TDB.l("反乱軍").$TD.GetArmyMessage($STATE->{rebel},"r");
$disp.=$TDB.l("状態").$TD."<SPAN>".l("反乱")."</SPAN>".$TRE;
	if ($STATE->{robinb} > $DT[$id2idx{$rebelid}]->{army})
	{
	$disp.=$TR.$TD.GetTagImgKao($BAL_NAME,"bal");
	$disp.="<td colspan=3><SPAN>".l("反乱リーダー")."</SPAN> ： <b>$BAL_NAME</b> <small>（$BAL_JOB）</small><br>";
	$disp.=">> ".l("領主の弱兵など相手にならんぞ！ぐわっはっは！");
	}
	else
	{
	$disp.=$TR.$TD.GetTagImgKao($DT[$id2idx{$rebelid}]->{name},$DT[$id2idx{$rebelid}]->{icon});
	$disp.="<td colspan=3><SPAN>".l("反乱リーダー")."</SPAN> ： <b>".$DT[$id2idx{$rebelid}]->{name}."</b>";
	$disp.=DignityDefine($DT[$id2idx{$rebelid}]->{dignity})." <small>（".$DT[$id2idx{$rebelid}]->{shopname}."）</small><br>";
	$disp.=">> ".$DT[$id2idx{$rebelid}]->{comment};
	}
	$disp.=$TRE;
}
else
{
$disp.=$TR.$TDB.l("反乱軍").$TD.l("不明");
$disp.=$TDB.l("状態").$TD.l("平穏").$TRE;
}
$disp.=$TBE;

if (!$GUEST_USER && $STATE->{leader}==$DT->{id})
	{
	$disp.=<<STR;
	<br>
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="lord-f">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=form VALUE="plus">
	<INPUT TYPE=SUBMIT VALUE='${\l('政務を執り行う')}'>
	</FORM>
STR
	}

OutSkin();
1;


sub GetTaxMessage
{
	my($per)=@_;
	
	return $per."%" if $MOBILE;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/r.gif" width="|.($per * 2).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100 - ($per * 2)).qq|" height="12">| if $per!=50;
	$bar.=" ".$per."%";
	$bar.="</nobr><br>";
	
	return $bar;
}

sub GetArmyMessage
{
	my($rank,$mode)=@_;
	return $rank.l("人") if $MOBILE;
	my $per=int($rank/500);
	$per=100 if $per>100;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/$mode.gif" width="|.(    $per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=200;
	$bar.=" ".$rank.l("人");
	$bar.="</nobr><br>";
	
	return $bar;
}
