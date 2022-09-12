use utf8;
# ドラゴンレース設定 2005/03/30 由來

# -------- 設定部分 ---------

# レース設定
@WEATHER=(l('晴'),l('雨'));
@RACERANK=(l('G1'),l('G2'),l('G3'),l('OP'),l('100下'),l('未勝利'));
@FIELDTYPE=(l('芝生'),l('ダート'));

@RACETERM=(l("登竜レース"),l("重賞レース"));

@RACE=(
	# 0名称		1ランク	2ハンデ	3馬場種	4終盤坂	5距離	6１着	7２着	8３着 9定員
	[
	[l("若葉新竜"),	,5	,0	,0	,1	,1600	,50	,30	,20	,10],
	[l("かさぶらんか杯"),,4	,20	,0	,0	,1600	,100	,50	,30	,10],
	[l("かさぶらんかダート杯"),,4,20	,1	,1	,1600	,100	,50	,30	,10],
	[l("未勝利2600ダート"),,5	,0	,1	,0	,2600	,50	,30	,20	,10],
	[l("あじさいカップ"),,3	,50	,0	,0	,2800	,150	,70	,50	,10],
	[l("あじさいダートカップ"),,3,50	,1	,0	,2800	,150	,70	,50	,10],
	[l("彩花新竜"),	,5	,0	,0	,0	,2200	,50	,30	,20	,10],
	[l("かえで杯"),	,4	,20	,0	,0	,2000	,100	,50	,30	,10],
	[l("かえでダート杯"),,4	,20	,1	,1	,2000	,100	,50	,30	,10],
	[l("未勝利1600ダート"),,5	,0	,1	,1	,1600	,50	,30	,20	,10],
	[l("あやめカップ"),,3	,50	,0	,1	,1400	,150	,70	,50	,10],
	[l("あやめダートカップ"),,3	,50	,1	,0	,1400	,150	,70	,50	,10],
	],
	[
	[l("酒場杯ハンデ"),	,2	,100	,0	,0	,2600	,200	,100	,80	,10],
	[l("水花賞"),	,2	,100	,1	,0	,2200	,200	,100	,80	,10],
	[l("新月杯"),	,2	,100	,0	,0	,1600	,200	,100	,80	,10],
	[l("蒼天杯"),	,2	,100	,0	,0	,2000	,200	,100	,80	,10],
	[l("領主チャレンジカップ"),,1,200	,0	,1	,2800	,300	,150	,100	,10],
	[l("桃花賞"),	,1	,200	,1	,0	,2200	,300	,150	,100	,10],
	[l("名月トライアルカップ"),,1,200	,0	,0	,1400	,300	,150	,100	,10],
	[l("黄天トライアルカップ"),,1,200	,0	,1	,2000	,300	,150	,100	,10],
	[l("新千年国王賞"),	,0	,0	,0	,0	,3000	,400	,200	,100	,10],
	[l("春花賞"),	,0	,0	,1	,1	,2400	,400	,200	,100	,10],
	[l("秋月賞"),	,0	,0	,0	,1	,1600	,400	,200	,100	,10],
	[l("霹靂賞"),	,0	,0	,0	,0	,2000	,400	,200	,100	,10],
	],
);

# 牧場
$RCest=1000000;

# 競争ドラゴン
$MYDRmax=3;
$DRbuy=500000;

# 引退
$DRretire=86400 * 10;
$PRentry=300;
$PRcycle=86400 * 3;

# 厩舎
$STest=500000;
$STcost=100000;
$STmax=10;
$STtime=86400 * 50;

# 騎手
$JKest=500000;
$JKmax=20;
$JKtime=86400 * 50;

# 騎手能力
@JKSP=(
	l("なし"),
	l("牝竜の騎乗が得意"),
	l("牡竜の騎乗が得意"),
	l("芝のレースに強い"),
	l("ダートのレースに強い"),
	l("大舞台に強い"),
	l("雨のレースに強い"),
	l("勝利すると竜の成長を促す"),
);

# 用語の定義

@STRATE=(l('逃げ'),l('先行'),l('差し'),l('追込'),l('自在'));

@EMPHA=(l('スピード'),l('勝負根性'),l('瞬発力'),l('パワー'),l('健康'),l('柔軟性'));

@VALUE=('Ｅ','Ｄ','Ｃ','Ｂ','Ａ','Ｓ','Ｓ');

@EVALUE=('×','△','○','◎','◎');

@FM=(l('牡'),l('牝'));

@ONRACE=(l('待機'),'<b>'.l('落選').'</b>','<SPAN>'.l('登録').'</SPAN>','<SPAN>'.l('出走').'</SPAN>');

@DRCOLOR=(l('紅毛'),l('青毛'),l('碧毛'),l('芦毛'),l('漆毛'));

# 更新時刻 (調教時刻 登竜出走締め 重賞出走締め)

@DRTIMESET=(3,23,22);

# -------- 設定完了 ---------

@DLOG=();

@DRnamelist=qw(
		no birth fm color name town owner stable race apt
		sp spp sr srp ag agp pw pwp hl hlp fl flp
		con wt gr
		prize sdwin g3win g2win g1win
		);

@PRnamelist=qw(
		no birth fm color name town owner apt hr preg
		sp sr ag pw hl fl
		prize sdwin g3win g2win g1win
		);

@RCnamelist=qw(
		no birth name town owner
		prize sdwin g3win g2win g1win
		);

@STnamelist=qw(
		no birth name town owner
		emp tr con wt
		sp sr ag pw hl fl
		sdwin g3win g2win g1win
		);

@JKnamelist=qw(
		no birth name town owner race
		ahead back sp
		sdwin g3win g2win g1win
		);

@RDnamelist=qw(
		no dr birth fm color name ranch rcname stable stname jock jkname prize strate
		sp1 sp2 sp3 sp4
		pop time str lose
		);
1;

sub GetTagImgDra
{
	my($i,$ii,$old)=@_;
	$i++;
	$ii++;
	$i+=2 if $old;
	return qq|<IMG class="i" SRC="$IMAGE_URL/dragon$i$ii$IMAGE_EXT">|;
}

