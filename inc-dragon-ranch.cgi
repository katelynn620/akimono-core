use utf8;
# ドラゴンレース 牧場メニュー表示 2005/03/30 由來

ReadRanch();
$disp.="<BIG>●".l('ドラゴンレース')."：".l('牧場')."</BIG><br><br>";

if ($MYRC==-1)
{
$disp.="$TB$TR$TD".GetTagImgKao(l("ドラゴン老師"),"slime1").$TD;
$disp.="<SPAN>".l('ドラゴン老師')."</SPAN>：".l('自分の牧場を持っていないようじゃな。')."<br>";
$disp.=l("牧場を持てば，自分のドラゴンを育てることができる。").$TRE.$TBE;
my $estmsg=GetMoneyString($RCest);
$disp.=<<STR;
<br>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="rcedit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>●${\l('牧場設立')}</BIG>： <INPUT TYPE=TEXT NAME=name SIZE=20> ${\l('と名付けて ')}
<INPUT TYPE=SUBMIT VALUE='${\l('設立')}'>
</FORM>
<br>
$TB$TR$TD
・${\l('牧場を設立するには，資金<b>%1</b>がかかります。',$estmsg)}<br>
・${\l('ドラゴンの育成には別途さらに資金がかかるので，余裕があるか考えてください。')}<br>
$TBE
STR
}
else
{
$disp.="$TB$TR$TDB".l('名称')."$TDB".l('創立')."$TDB".l('平均賞金')."$TDB".l('総賞金')."$TDB".l('成績')."$TRE";
$disp.=$TR;
$disp.=$TD.$RC[$MYRC]->{name};
$disp.=$TD.GetTime2found($NOW_TIME-$RC[$MYRC]->{birth});
$disp.=$TD.($RC[$MYRC]->{aprize} + 0).l("万");
$disp.=$TD.($RC[$MYRC]->{prize} + 0).l("万");
$disp.=$TD.($RC[$MYRC]->{g1win} + 0)." - ".($RC[$MYRC]->{g2win} + 0)." - ".($RC[$MYRC]->{g3win} + 0)." - ".($RC[$MYRC]->{sdwin} + 0);
$disp.=$TRE.$TBE;
$disp.="<br><BIG>●".l('所有競争竜')."</BIG><br><br>";
ReadDragon();
if (!scalar @MYDR)
	{
	$disp.=l("所有の競争竜はありません")."<br><br>";
	}
	else
	{
$disp.="$TB$TR$TDB".l('名称')."$TDB".l('年齢')."$TDB".l('性別')."$TDB".l('スピ')."$TDB".l('勝負')."$TDB".l('瞬発')."$TDB".l('パワ')."$TDB".l('体調')."$TDB".l('体重')."$TDB".l('距離適性')."$TDB".l('総賞金')."$TDB".l('成績')."$TRE";
	foreach (@MYDR)
		{
$disp.=$TR;
$disp.=$TD."<a href=\"action.cgi?key=slime&mode=detail&dr=$DR[$_]->{no}&$USERPASSURL\">"
	.GetTagImgDra($DR[$_]->{fm},$DR[$_]->{color}).$DR[$_]->{name}."</a>";
$disp.=$TD.GetTime2found($NOW_TIME-$DR[$_]->{birth});
$disp.=$TD.$FM[$DR[$_]->{fm}];
$disp.=$TD.$VALUE[int($DR[$_]->{sp} /100*6)];
$disp.=$TD.$VALUE[int($DR[$_]->{sr} /100*6)];
$disp.=$TD.$VALUE[int($DR[$_]->{ag} /100*6)];
$disp.=$TD.$VALUE[int($DR[$_]->{pw} /100*6)];
$disp.=$TD.$EVALUE[int($DR[$_]->{con} /100*4)];
$disp.=$TD.$DR[$_]->{wt};
$disp.=$TD.GetRaceApt($DR[$_]->{apt},$DR[$_]->{fl});
$disp.=$TD.($DR[$_]->{prize} + 0).l("万");
$disp.=$TD.($DR[$_]->{g1win} + 0)." - ".($DR[$_]->{g2win} + 0)." - ".($DR[$_]->{g3win} + 0)." - ".($DR[$_]->{sdwin} + 0);
$disp.=$TRE;
		}
$disp.=$TBE."<br>";
	}

ReadParent();

if (scalar @MYPR)
	{
	$disp.="<BIG>●".l('所有繁殖%1竜',$FM[1])."</BIG><br><br>";
$disp.="$TB$TR$TDB".l('名称')."$TDB".l('年齢')."$TDB".l('遺伝')."$TDB".l('スピ')."$TDB".l('勝負')."$TDB".l('瞬発')."$TDB".l('パワ')."$TDB".l('健康')."$TDB".l('柔軟')."$TDB".l('距離適性')."$TDB".l('現役賞金')."$TDB".l('現役成績')."$TRE";
	foreach (@MYPR)
		{
$disp.=$TR;
$disp.=$TD."<a href=\"action.cgi?key=slime&mode=pr&dr=$PR[$_]->{no}&$USERPASSURL\">"
	.GetTagImgDra($PR[$_]->{fm},$PR[$_]->{color},1).$PR[$_]->{name}."</a>";
$disp.=$TD.GetTime2found($NOW_TIME-$PR[$_]->{birth});
$disp.=$TD.$VALUE[int($PR[$_]->{hr} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{sp} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{sr} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{ag} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{pw} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{hl} /100*6)];
$disp.=$TD.$VALUE[int($PR[$_]->{fl} /100*6)];
$disp.=$TD.GetRaceApt($PR[$_]->{apt},$PR[$_]->{fl});
$disp.=$TD.($PR[$_]->{prize} + 0).l("万");
$disp.=$TD.($PR[$_]->{g1win} + 0)." - ".($PR[$_]->{g2win} + 0)." - ".($PR[$_]->{g3win} + 0)." - ".($PR[$_]->{sdwin} + 0);
$disp.=$TRE;
		}
$disp.=$TBE."<br>";
	}



if (scalar @MYDR < $MYDRmax)
	{
my @dist=(l('短距離竜'),l('中距離竜'),l('長距離竜'));
my $formdist="";
foreach(0..$#dist) {$formdist.=qq|<OPTION VALUE="$_">$dist[$_]|; }
my $buymsg=GetMoneyString($DRbuy);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="dredit">
<INPUT TYPE=HIDDEN NAME=code VALUE="new">
<BIG>●${\l('ドラゴン購入')}</BIG>： <SELECT NAME=fm SIZE=1>
<OPTION VALUE="0">$FM[0]<OPTION VALUE="1">$FM[1]
</SELECT> ${\l('の')} <SELECT NAME=dist SIZE=1>
$formdist
</SELECT> ${\l('を')} 
<INPUT TYPE=TEXT NAME=name SIZE=20> ${\l('と名付けて')} 
<INPUT TYPE=SUBMIT VALUE='${\l('購入')}'>
</FORM>
<br>
$TB$TR$TD
・${\l('競争竜は，<b>%1</b>頭まで持つことができます。',$MYDRmax)}<br>
・${\l('購入するには，資金<b>%1</b>がかかります。',$buymsg)}<br>
・${\l('名前は，<b>全角カタカナ10文字</b>以内です。')}
$TBE
STR
	}
}
1;



