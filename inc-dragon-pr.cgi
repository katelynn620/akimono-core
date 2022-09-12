use utf8;
# ドラゴンレース 隠居ドラゴン詳細表示 2005/03/30 由來

$disp.="<BIG>●".l('ドラゴンレース')."：".l('牧場')."</BIG><br><br>";

ReadParent();
my $cnt=$id2pr{$Q{dr}};
OutError('bad request') if ($MYDIR ne $PR[$cnt]->{town});
OutError('bad request') if ($PR[$cnt]->{owner}!=$DT->{id});
OutError('bad request') if (!$PR[$cnt]->{fm});

$forment="";
foreach(0..$PRcount)
	{
	next if $PR[$_]->{fm};
	$forment.="<OPTION VALUE=\"$PR[$_]->{no}\">$PR[$_]->{name}";
	}

$disp.="$TB$TR$TDB".l('名称')."$TDB".l('年齢')."$TDB".l('毛色')."$TDB".l('脚質')."$TDB".l('距離適性')."$TDB".l('現役賞金')."$TDB".l('現役成績')."$TDB".l('前回の出産')."$TRE";
$disp.=$TR;
$disp.=$TD."<b>".GetTagImgDra($PR[$cnt]->{fm},$PR[$cnt]->{color},1).$PR[$cnt]->{name}."</b>";
$disp.=$TD.GetTime2found($NOW_TIME-$PR[$cnt]->{birth});
$disp.=$TD.$DRCOLOR[$PR[$cnt]->{color}];
$disp.=$TD.$STRATE[ GetRaceStrate($PR[$cnt]->{sr},$PR[$cnt]->{ag}) ];
$disp.=$TD.GetRaceApt($PR[$cnt]->{apt},$PR[$cnt]->{fl})."km";
$disp.=$TD.($PR[$cnt]->{prize} + 0)."万";
$disp.=$TD.($PR[$cnt]->{g1win} + 0)." - ".($PR[$cnt]->{g2win} + 0)." - ".($PR[$cnt]->{g3win} + 0)." - ".($PR[$cnt]->{sdwin} + 0);
$disp.=$TD.GetTime2FormatTime($PR[$cnt]->{preg});
$disp.=$TRE;
$disp.=$TBE."<br>";
$disp.="<BIG>●".l('能力の詳細')."</BIG><br><br>";
$disp.=$TB;
$disp.=$TR.$TDB.l('遺伝力').$TD.GetParentBar($PR[$cnt]->{hr}).$TRE;
$disp.=$TR.$TDB.l('スピード').$TD.GetParentBar($PR[$cnt]->{sp}).$TRE;
$disp.=$TR.$TDB.l('勝負根性').$TD.GetParentBar($PR[$cnt]->{sr}).$TRE;
$disp.=$TR.$TDB.l('瞬発力').$TD.GetParentBar($PR[$cnt]->{ag}).$TRE;
$disp.=$TR.$TDB.l('パワー').$TD.GetParentBar($PR[$cnt]->{pw}).$TRE;
$disp.=$TR.$TDB.l('健康').$TD.GetParentBar($PR[$cnt]->{hl}).$TRE;
$disp.=$TR.$TDB.l('柔軟性').$TD.GetParentBar($PR[$cnt]->{fl}).$TRE;
$disp.=$TBE."<br>";
if ($forment && ($NOW_TIME-$PR[$cnt]->{preg} > $PRcycle))
	{
	FormPreg();
	}
1;

sub GetParentBar
{
	my($per)=@_;
	
	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/b.gif" width="|.($per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100;
	$bar.=" ".($per + 0);
	$bar.="</nobr>";
	return $bar;
}

sub FormPreg
{
my $prmsg=GetTime2found($PRcycle);
$disp.=<<STR;
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="slime-s">
<INPUT TYPE=HIDDEN NAME=bk VALUE="slime">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="predit">
<INPUT TYPE=HIDDEN NAME=code VALUE="preg">
<INPUT TYPE=HIDDEN NAME=dr VALUE="$Q{dr}">
<BIG>●${\l('種付け')}</BIG>： ${\l('生まれるドラゴンを')} 
<INPUT TYPE=TEXT NAME=name SIZE=20> ${\l('と名付けて')} 
<SELECT NAME=pr SIZE=1>
$forment
</SELECT> ${\l('を')} 
<INPUT TYPE=SUBMIT VALUE='${\l('種付けする')}'>
</FORM>
<br>
$TB$TR$TD
・${\l('競争竜がすでに <b>%1</b>頭いるときは，種付けを実行できません。',$MYDRmax)}<br>
・${\l('名前は，<b>ひらがな10文字</b>以内です。')}<br>
・${\l('種%1竜の所有者に，種付け料を支払います。',$FM[0])}<br>
・${\l('出産すると，<b>%1</b>間は次の種付けができません。',$prmsg)}
$TBE<br>
STR
}

