use utf8;
# ドラゴンレース 厩舎メニュー表示 2005/03/30 由來

ReadStable();
$disp.="<BIG>●".l('ドラゴンレース')."：".l('厩舎')."</BIG><br><br>";

if ($MYST==-1)
{
$disp.="$TB$TR$TD".GetTagImgKao(l("ドラゴン調教師"),"slime3").$TD;
$disp.="<SPAN>".l('ドラゴン調教師')."</SPAN>：".l('自分の厩舎を持っていないようだな。')."<br>";
$disp.=l("厩舎を持てば，自分や他人のドラゴンを調教することができる。").$TRE.$TBE."<br>";
if (scalar @ST < $STmax)
	{
	FormStable();
	}
	else
	{
	$disp.="<BIG>●".l('厩舎設立')."</BIG>： ".l("定数に達しているため，これ以上設立できません。");
	}
}
else
{
	$disp.="$TB$TR$TDB".l('名称')."$TDB".l('方針')."$TDB".l('調教')."$TDB".l('体調')."$TDB".l('体重')."$TDB".l('コース')."$TDB".l('併竜')."$TDB".l('坂路')."$TDB".l('ダート')."$TDB".l('温泉')."$TDB".l('繋養')."$TDB".l('成績')."$TDB".l('維持費')."$TDB".l('老朽化')."$TRE";
	$disp.=$TR;
	$disp.=$TD.$ST[$MYST]->{name};
	$disp.=$TD.$EMPHA[$ST[$MYST]->{emp}];
	$disp.=$TD.$VALUE[int($ST[$MYST]->{tr} /100*6)];
	$disp.=$TD.$VALUE[int($ST[$MYST]->{con} /100*6)];
	$disp.=$TD.$VALUE[int($ST[$MYST]->{wt} /100*6)];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{sp}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{sr}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{ag}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{pw}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{hl}];
	$disp.=$TD.$EVALUE[$ST[$MYST]->{fl}];
	$disp.=$TD.($ST[$MYST]->{g1win} + 0)." - ".($ST[$MYST]->{g2win} + 0)." - ".($ST[$MYST]->{g3win} + 0)." - ".($ST[$MYST]->{sdwin} + 0);
	$cost=($ST[$MYST]->{sp} + $ST[$MYST]->{sr} + $ST[$MYST]->{ag} + $ST[$MYST]->{pw} + $ST[$MYST]->{hl} + $ST[$MYST]->{fl});
	$disp.=$TD.GetMoneyString($cost * $STcost);
	my $limit=$ST[$MYST]->{birth} + $STtime - $NOW_TIME;
	$disp.=$TD.l("あと %1",(($limit > 0) ? GetTime2found($limit)) : l("わずか"));
	$disp.=$TRE.$TBE."<br>";
	StableDragon();
	FormLarge();
}
1;

sub FormStable
{
my $estmsg=GetMoneyString($STest);
my $costmsg=GetMoneyString($STcost);
my $formemp;
	foreach (0..$#EMPHA)
	{
	$formemp.="<OPTION VALUE=\"$_\">$EMPHA[$_]";
	}
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="stedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>●${\l('厩舎設立')}</BIG>： <SELECT NAME=emp SIZE=1>
$formemp
</SELECT> ${\l('を調教方針とする厩舎を')} <INPUT TYPE=TEXT NAME=name SIZE=20> ${\l('と名付けて')} 
<INPUT TYPE=SUBMIT VALUE='${\l('設立')}'>
</FORM>
<br>
$TB$TR$TD
・${\l('厩舎を設立するには，資金<b>%1</b>がかかります。',$estmsg)}<br>
・${\l('維持費が最低でも毎日<b>%1</b>かかります。',$costmsg)}<br>
・${\l('調教方針を選べます。後から変更することはできません。')}<br>
・${\l('厩舎は全体で <b>%1</b>舎の上限があり，満杯になると設立できません。',$STmax)}
$TBE
STR
}

sub StableDragon
{
	$disp.="<BIG>●".l('入厩中の竜')."</BIG><br><br>";
	ReadDragon();
	$disp.="$TB$TR$TDB".l('名称')."$TDB".l('年齢')."$TDB".l('性別')."$TDB".l('体調')."$TDB".l('体重')."$TDB".l('総賞金')."$TDB".l('成績')."$TRE";
	foreach(0..$#DR)
	{
	next if ($DR[$_]->{stable} != $ST[$MYST]->{no});
$disp.=$TR;
$disp.=$TD.GetTagImgDra($DR[$_]->{fm},$DR[$_]->{color}).$DR[$_]->{name};
$disp.=$TD.GetTime2found($NOW_TIME-$DR[$_]->{birth});
$disp.=$TD.$FM[$DR[$_]->{fm}];
$disp.=$TD.$EVALUE[int($DR[$_]->{con} /100*4)];
$disp.=$TD.$DR[$_]->{wt};
$disp.=$TD.($DR[$_]->{prize} + 0).l("万");
$disp.=$TD.($DR[$_]->{g1win} + 0)." - ".($DR[$_]->{g2win} + 0)." - ".($DR[$_]->{g3win} + 0)." - ".($DR[$_]->{sdwin} + 0);
$disp.=$TRE;
	}
$disp.=$TBE."<br>";
}


sub FormLarge
{
my $n=int(($NOW_TIME - $ST[$MYST]->{birth})/86400/2) + 1;
if ($n < $cost)
	{
	$disp.="<BIG>●".l('厩舎増築')."</BIG>： ".l("まだこれ以上の増築はできません");
	return;
	}
my $estmsg=GetMoneyString($STest);
my @LARGE=(
	l('トラックコース (スピード上昇)'),
	l('併せ竜 (勝負根性上昇)'),
	l('坂路施設 (瞬発力上昇)'),
	l('ダートトラック (パワー上昇)'),
	l('温泉施設 (健康上昇)'),
	l('繋養施設 (柔軟性上昇)')
);
my $formemp;
	foreach (0..$#LARGE)
	{
	$formemp.="<OPTION VALUE=\"$_\">$LARGE[$_]";
	}
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="stedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="large">
<BIG>●${\l('厩舎増築')}</BIG>： <SELECT NAME=lar SIZE=1>
$formemp
</SELECT> ${\l('を')} <INPUT TYPE=SUBMIT VALUE='${\l('増築')}'>
</FORM>
<br>
$TB$TR$TD
・${\l('厩舎を増築するには，資金<b>%1</b>がかかります。',$estmsg)}<br>
・${\l('増築すると維持費が多くかかるようになります。')}<br>
・${\l('預託料の収入より維持費が上回ると，赤字になるのでご注意ください。')}
$TBE
STR
}

