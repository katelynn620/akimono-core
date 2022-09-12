use utf8;
# ドラゴンレース 騎手メニュー表示 2005/03/30 由來

ReadJock();
$disp.="<BIG>●".l('ドラゴンレース')."：".l('騎手')."</BIG><br><br>";

if ($MYJK==-1)
{
$disp.="$TB$TR$TD".GetTagImgKao(l("騎手仲間"),"slime5").$TD;
$disp.="<SPAN>".l('騎手仲間')."</SPAN>：".l('騎手を雇っていないんだな。')."<br>";
$disp.=l("騎手を雇えば，自分や他人のドラゴンの力をレースで引き出せる。").$TRE.$TBE."<br>";
if (scalar @JK < $JKmax)
	{
	FormJock();
	}
	else
	{
	$disp.="<BIG>●".l('騎手雇用')."</BIG>： ".l('定員に達しているため，これ以上雇用できません。')."";
	}
}
else
{
$disp.="$TB$TR$TDB".l('名前')."$TDB".l('勤続')."$TDB".l('逃先')."$TDB".l('差追')."$TDB".l('成績')."$TDB".l('特殊能力')."$TDB".l('出走')."$TRE";
$disp.=$TR;
$disp.=$TD.$JK[$MYJK]->{name};
$disp.=$TD.GetTime2found($NOW_TIME-$JK[$MYJK]->{birth});
$disp.=$TD.$VALUE[int($JK[$MYJK]->{ahead} /100*6)];
$disp.=$TD.$VALUE[int($JK[$MYJK]->{back} /100*6)];
$disp.=$TD.($JK[$MYJK]->{g1win} + 0)." - ".($JK[$MYJK]->{g2win} + 0)." - ".($JK[$MYJK]->{g3win} + 0)." - ".($JK[$MYJK]->{sdwin} + 0);
$disp.=$TD."<small>".$JKSP[($JK[$MYJK]->{sp} + 0)]."</small>";
$disp.=$TD.$ONRACE[$JK[$MYJK]->{race}];
$disp.=$TRE.$TBE;
}
1;

sub FormJock
{
my $estmsg=GetMoneyString($JKest);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="jkedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>●${\l('騎手雇用')}</BIG>： <INPUT TYPE=TEXT NAME=name SIZE=20> ${\l('と名付けて')} 
<INPUT TYPE=SUBMIT VALUE='${\l('雇用')}'>
</FORM>
<br>
$TB$TR$TD
・${\l('騎手を雇用するには，資金<b>%1</b>がかかります。',$estmsg)}<br>
・${\l('騎手は全体で <b>%1</b>人の定員があり，満員になると雇用できません。',$JKmax)}
$TBE
STR
}

