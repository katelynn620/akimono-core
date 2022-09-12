use utf8;
# ドラゴンレース 情報ウインドウ 2005/03/30 由來

$NOITEM=1;
$NOMENU=1;
$Q{bk}="none";
RequireFile('inc-dragon.cgi');
DataRead();
CheckUserPass(1);

my $functionname=$Q{mode};
&$functionname if defined(&$functionname);
OutSkin();
1;

sub st
{
	ReadStable();
	@ST=sort{$b->{win}<=>$a->{win}}@ST;
	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar @ST);
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"mode=st","",$pagemax,$page);

	$disp.=<<STR;
<BIG>●${\l('ドラゴンレース')}：${\l('厩舎一覧')}</BIG><br><br>
$pagecontrol
$TB$TR$TDB${\l('名称')}$TDB${\l('方針')}$TDB${\l('調教')}$TDB${\l('体調')}$TDB${\l('体重')}$TDB${\l('コース')}$TDB${\l('併竜')}$TDB${\l('坂路')}$TDB${\l('ダート')}$TDB${\l('温泉')}$TDB${\l('繋養')}$TDB${\l('成績')}$TRE
STR

	foreach my $i($pagestart..$pageend)
		{
		next if !$ST[$i]->{name};
		$disp.=$TR;
		$disp.=$TD.$ST[$i]->{name};
		$disp.=$TD.$EMPHA[$ST[$i]->{emp}];
		$disp.=$TD.$VALUE[int($ST[$i]->{tr} /100*6)];
		$disp.=$TD.$VALUE[int($ST[$i]->{con} /100*6)];
		$disp.=$TD.$VALUE[int($ST[$i]->{wt} /100*6)];
		$disp.=$TD.$EVALUE[$ST[$i]->{sp}];
		$disp.=$TD.$EVALUE[$ST[$i]->{sr}];
		$disp.=$TD.$EVALUE[$ST[$i]->{ag}];
		$disp.=$TD.$EVALUE[$ST[$i]->{pw}];
		$disp.=$TD.$EVALUE[$ST[$i]->{hl}];
		$disp.=$TD.$EVALUE[$ST[$i]->{fl}];
		$disp.=$TD.($ST[$i]->{g1win} + 0)." - ".($ST[$i]->{g2win} + 0)." - ".($ST[$i]->{g3win} + 0)." - ".($ST[$i]->{sdwin} + 0);
		}
	$disp.=$TRE.$TBE;
	$disp.=$pagecontrol;
}

sub dra
{
	ReadDragon();
	@DR=sort{$a->{name} cmp $b->{name}}@DR;
	@DR=sort{$b->{prize}<=>$a->{prize}}@DR;
	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar @DR);
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"mode=dra","",$pagemax,$page);

	$disp.=<<STR;
<BIG>●${\l('ドラゴンレース')}：${\l('競争竜一覧')}</BIG><br><br>
$pagecontrol
$TB$TR$TDB${\l('名称')}$TDB${\l('年齢')}$TDB${\l('性別')}$TDB${\l('スピ')}$TDB${\l('勝負')}$TDB${\l('瞬発')}$TDB${\l('パワ')}$TDB${\l('体調')}$TDB${\l('体重')}$TDB${\l('距離適性')}$TDB${\l('総賞金')}$TDB${\l('成績')}$TRE
STR

	foreach ($pagestart..$pageend)
		{
		next if !$DR[$_]->{name};
		$disp.=$TR;
		$disp.=$TD.GetTagImgDra($DR[$_]->{fm},$DR[$_]->{color}).$DR[$_]->{name};
		$disp.=$TD.GetTime2found($NOW_TIME-$DR[$_]->{birth});
		$disp.=$TD.$FM[$DR[$_]->{fm}];
		$disp.=$TD.$VALUE[int($DR[$_]->{sp} /100*6)];
		$disp.=$TD.$VALUE[int($DR[$_]->{sr} /100*6)];
		$disp.=$TD.$VALUE[int($DR[$_]->{ag} /100*6)];
		$disp.=$TD.$VALUE[int($DR[$_]->{pw} /100*6)];
		$disp.=$TD.$EVALUE[int($DR[$_]->{con} /100*4)];
		$disp.=$TD.$DR[$_]->{wt};
		$disp.=$TD.GetRaceApt($DR[$_]->{apt},$DR[$_]->{fl});
		$disp.=$TD.l("%1万",($DR[$_]->{prize} + 0));
		$disp.=$TD.($DR[$_]->{g1win} + 0)." - ".($DR[$_]->{g2win} + 0)." - ".($DR[$_]->{g3win} + 0)." - ".($DR[$_]->{sdwin} + 0);
		$disp.=$TRE;
		}
	$disp.=$TBE;
}

sub pr
{
	ReadParent();
	@PR=sort{$b->{prize}<=>$a->{prize}}@PR;
	@PR=sort{$a->{fm}<=>$b->{fm}}@PR;
	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar @PR);
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"mode=pr","",$pagemax,$page);

	$disp.=<<STR;
<BIG>●${\l('ドラゴンレース')}：${\l('隠居竜一覧')}</BIG><br><br>
$pagecontrol
$TB$TR$TDB${\l('名称')}$TDB${\l('年齢')}$TDB${\l('性別')}$TDB${\l('スピ')}$TDB${\l('勝負')}$TDB${\l('瞬発')}$TDB${\l('パワ')}$TDB${\l('健康')}$TDB${\l('柔軟')}$TDB${\l('距離適性')}$TDB${\l('現役賞金')}$TDB${\l('現役成績')}$TRE
STR

	foreach ($pagestart..$pageend)
		{
		next if !$PR[$_]->{name};
		$disp.=$TR;
		$disp.=$TD.GetTagImgDra($PR[$_]->{fm},$PR[$_]->{color},1).$PR[$_]->{name};
		$disp.=$TD.GetTime2found($NOW_TIME-$PR[$_]->{birth});
		$disp.=$TD.($PR[$_]->{fm} ? l("繁殖") : l("種")).$FM[$PR[$_]->{fm}];
		$disp.=$TD.$VALUE[int($PR[$_]->{sp} /100*6)];
		$disp.=$TD.$VALUE[int($PR[$_]->{sr} /100*6)];
		$disp.=$TD.$VALUE[int($PR[$_]->{ag} /100*6)];
		$disp.=$TD.$VALUE[int($PR[$_]->{pw} /100*6)];
		$disp.=$TD.$VALUE[int($PR[$_]->{hl} /100*6)];
		$disp.=$TD.$VALUE[int($PR[$_]->{fl} /100*6)];
		$disp.=$TD.GetRaceApt($PR[$_]->{apt},$PR[$_]->{fl});
		$disp.=$TD.l("%1万",($PR[$_]->{prize} + 0));
		$disp.=$TD.($PR[$_]->{g1win} + 0)." - ".($PR[$_]->{g2win} + 0)." - ".($PR[$_]->{g3win} + 0)." - ".($PR[$_]->{sdwin} + 0);
		$disp.=$TRE;
		}
	$disp.=$TBE;
}

sub jk
{
	ReadJock();
	@JK=sort{$b->{win}<=>$a->{win}}@JK;
	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar @JK);
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"mode=jk","",$pagemax,$page);

	$disp.=<<STR;
<BIG>●${\l('ドラゴンレース')}：${\l('騎手一覧')}</BIG><br><br>
$pagecontrol
$TB$TR$TDB${\l('名前')}$TDB${\l('勤続')}$TDB${\l('逃先')}$TDB${\l('差追')}$TDB${\l('成績')}$TDB${\l('特殊能力')}$TDB${\l('出走')}$TRE
STR

	foreach my $i($pagestart..$pageend)
		{
		next if !$JK[$i]->{name};
		$disp.=$TR;
		$disp.=$TD.$JK[$i]->{name};
		$disp.=$TD.GetTime2found($NOW_TIME-$JK[$i]->{birth});
		$disp.=$TD.$VALUE[int($JK[$i]->{ahead} /100*6)];
		$disp.=$TD.$VALUE[int($JK[$i]->{back} /100*6)];
		$disp.=$TD.($JK[$i]->{g1win} + 0)." - ".($JK[$i]->{g2win} + 0)." - ".($JK[$i]->{g3win} + 0)." - ".($JK[$i]->{sdwin} + 0);
		$disp.=$TD."<small>".$JKSP[($JK[$i]->{sp} + 0)]."</small>";
		$disp.=$TD.$ONRACE[$JK[$i]->{race}];
		$disp.=$TRE;
		}
	$disp.=$TBE;
	$disp.=$pagecontrol;
}

sub rc
{
	ReadRanch();
	@RC=sort{$b->{aprize}<=>$a->{aprize}}@RC;
	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar @RC);
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"mode=rc","",$pagemax,$page);

	$disp.=<<STR;
<BIG>●${\l('ドラゴンレース')}：${\l('牧場一覧')}</BIG><br><br>
$pagecontrol
$TB$TR$TDB${\l('名称')}$TDB${\l('所属')}$TDB${\l('創立')}$TDB${\l('平均賞金')}$TDB${\l('総賞金')}$TDB${\l('成績')}$TRE
STR

	foreach my $i($pagestart..$pageend)
		{
		next if !$RC[$i]->{name};
		$disp.=$TR;
		$disp.=$TD.$RC[$i]->{name};
		$disp.=$TD.$Tname{$RC[$i]->{town}};
		$disp.=$TD.GetTime2found($NOW_TIME-$RC[$i]->{birth});
		$disp.=$TD.l("%1万",($RC[$i]->{aprize} + 0));
		$disp.=$TD.l("%1万",($RC[$i]->{prize} + 0));
		$disp.=$TD.($RC[$i]->{g1win} + 0)." - ".($RC[$i]->{g2win} + 0)." - ".($RC[$i]->{g3win} + 0)." - ".($RC[$i]->{sdwin} + 0);
		$disp.=$TRE;
		}
	$disp.=$TBE;
	$disp.=$pagecontrol;
}

sub sche
{
	$disp.="<BIG>●${\l('ドラゴンレース')}：${\l('スケジュール')}</BIG><br><br>";

	my $fn=GetPath($COMMON_DIR,"dr-last");
	require $fn if (-e $fn);
	$disp.=$TB;
	foreach (0..$#DRTIME)
		{
		$disp.=$TR;
		$disp.=$TDB.($_ ? l("次の%1変動時刻",$RACETERM[($_ - 1)]) : l("次の調教時刻"));
		$disp.=$TD.GetTime2FormatTime($DRTIME[$_]);
		$disp.=$TRE;
		}
	$disp.=$TBE."<br>";

	foreach (0..$#RACE)
		{
		$disp.="<BIG>●".l("%1開催日程",$RACETERM[($_)])."</BIG><br><br>";
		$disp.="$TB$TR$TDB${\l('名称')}$TDB${\l('ランク')}$TDB${\l('ハンデ')}$TDB${\l('馬場種')}$TDB${\l('坂')}$TDB${\l('距離')}$TDB${\l('%1着賞金','１')}$TDB${\l('%1着賞金','２')}$TDB${\l('%1着賞金','３')}$TDB${\l('定員')}$TRE";
		my @MYRACE=@{$RACE[$_]};
		foreach my $i(0..$#MYRACE)
			{
			my @R=@{$MYRACE[$i]};
			$disp.=$TR;
			$disp.=$TD.$R[0];
			$disp.=$TD.$RACERANK[$R[1]];
			$disp.=$TD.($R[2] ? l("%1万毎",$R[2]) : " ");
			$disp.=$TD.$FIELDTYPE[$R[3]];
			$disp.=$TD.($R[4] ? l("あり") : " ");
			$disp.=$TD.$R[5];
			$disp.=$TD.l("%1万",$R[6]);
			$disp.=$TD.l("%1万",$R[7]);
			$disp.=$TD.l("%1万",$R[8]);
			$disp.=$TD.$R[9];
			$disp.=$TRE;
			}
		$disp.=$TBE."<br>";
		}
}

sub rd
{
	my $rcode=$Q{rcode};
	$rcode||=0;
	ReadRace($rcode);
	ReadDragon();

	$disp.=<<STR;
<BIG>●${\l('ドラゴンレース')}：${\l('出走竜詳細',$RACETERM[$rcode])}</BIG><br><br>
$TB$TR$TDB${\l('名称')}$TDB${\l('年齢')}$TDB${\l('性別')}$TDB${\l('スピ')}$TDB${\l('勝負')}$TDB${\l('瞬発')}$TDB${\l('パワ')}$TDB${\l('体調')}$TDB${\l('体重')}$TDB${\l('距離適性')}$TRE
STR

foreach (0..$#RD)
	{
	next if !$RD[$_]->{name};
	next if (!defined $id2dra{$RD[$_]->{dr}});
	my $i=$id2dra{$RD[$_]->{dr}};
	$disp.=$TR;
	$disp.=$TD.GetTagImgDra($DR[$i]->{fm},$DR[$i]->{color}).$DR[$i]->{name};
	$disp.=$TD.GetTime2found($NOW_TIME-$DR[$i]->{birth});
	$disp.=$TD.$FM[$DR[$i]->{fm}];
	$disp.=$TD.$VALUE[int($DR[$i]->{sp} /100*6)];
	$disp.=$TD.$VALUE[int($DR[$i]->{sr} /100*6)];
	$disp.=$TD.$VALUE[int($DR[$i]->{ag} /100*6)];
	$disp.=$TD.$VALUE[int($DR[$i]->{pw} /100*6)];
	$disp.=$TD.$EVALUE[int($DR[$i]->{con} /100*4)];
	$disp.=$TD.$DR[$i]->{wt};
	$disp.=$TD.GetRaceApt($DR[$i]->{apt},$DR[$i]->{fl});
	$disp.=$TRE;
	}
$disp.=$TBE;
}

