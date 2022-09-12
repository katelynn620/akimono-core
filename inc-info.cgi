use utf8;
# 店舗情報 2005/01/06 由來

$disp.="<BIG>●".l('店舗情報')."</BIG><br><br>";

my $tm=$NOW_TIME-$DT->{time};
if($tm<0)
{
	$tm=-$tm;
	$tm=l('行動可能まであと %1',GetTime2HMS($tm));
}else{
	if($tm>$MAX_STOCK_TIME){$tm=$MAX_STOCK_TIME;}
	$tm=GetTime2HMS($tm);
}
my $rankmsg=GetRankMessage($DT->{rank});

my $expsum=0;
foreach(values(%{$DT->{exp}})){$expsum+=$_;}
$expsum=int($expsum/10)."%";

my $job=l("すっぴん");
$job=$JOBTYPE{$DT->{job}} if ($DT->{job});

my $level=DignityDefine($DT->{dignity},2);
$level=$DIGNITY[0] if !$level;

if(!$MOBILE)
{
	my @taxmode=('',l('(免税)'),l('(倍税)'));
	$disp.=$TB;
	$disp.=$TR;
	$disp.="<td width=48 rowspan=2>".GetTagImgKao($DT->{name},$DT->{icon});
	$disp.="<td align=center colspan=4><SPAN>RANK ".($id2idx{$DT->{id}}+1)."</SPAN> ： ".GetTagImgGuild($DT->{guild})."<b>".$DT->{shopname}."</b>";
	$disp.="<td align=center rowspan=2>".GetTagImgJob($DT->{job},$DT->{icon}).$TRE;
	$disp.=$TR."<td width=56 class=b>".l('爵位')."$TD$level <small>(".l('経験値')." ".($DT->{dignity}+0)."pt)";
	$disp.=$TDB.l('ジョブ').'<td width=64>'.$job.$TRE;
	$disp.=$TR."<td colspan=2 class=b>".l('点数').$TD.$DT->{point}.$TDB.l("資金");
	$disp.=$DT->{money}>=0 ? "<td colspan=2>".GetMoneyString($DT->{money}).$TRE : "<td colspan=2><font color=\"#cc2266\"><b>-".GetMoneyString(-$DT->{money})."</b></font>".$TRE;
	$disp.=$TR."<td colspan=2 class=b>".l('持ち時間').$TD.$tm.$TDB.l("創業")."<td colspan=2>".GetTime2HMS($NOW_TIME-$DT->{foundation}).$TRE;
	$disp.=$TR."<td colspan=2 class=b>".l('人気').$TD.$rankmsg.$TDB.l("ごみ")."<td colspan=2>".GetCleanMessage($DT->{trush}).$TRE;
	$disp.=$TR."<td colspan=2 class=b>".l('今期売上').$TD.GetMoneyString($DT->{saletoday}).$TDB.l('前期売上')."<td colspan=2>$term[0]".$DT->{saleyesterday}."$term[1]".$TRE;
	$disp.=$TR."<td colspan=2 class=b>".l('今期支払').$TD.GetMoneyString($DT->{paytoday}).$TDB.l('前期支払')."<td colspan=2>$term[0]".$DT->{payyesterday}."$term[1]".$TRE;
	$disp.=$TR."<td colspan=2 class=b>".l('今期維持費')."<BR><SMALL>(決算時徴収)</SMALL>".$TD.GetMoneyString(int($DT->{costtoday}))."+".GetMoneyString($SHOWCASE_COST[$DT->{showcasecount}-1]);
	$disp.=   $TDB.l('前期維持費')."<td colspan=2>$term[0]".$DT->{costyesterday}."$term[1]".$TRE;
	$disp.=$TR."<td colspan=2 class=b>".l('今期売却税').$TD.GetMoneyString($DT->{taxtoday}).$TDB.l('前期売却税')."<td colspan=2>$term[0]".($DT->{taxyesterday}+0)."$term[1]".$TRE;
	$disp.=$TR."<td colspan=2 class=b>".l('基本売却税率').$TD.GetUserTaxRate($DT,$DTTaxrate).'%'.$taxmode[$DT->{taxmode}+0].$TDB.l("熟練度合計")."<td colspan=2>".$expsum.$TRE;
	$disp.=$TR."<td colspan=2 class=b>".l('優勝回数').$TD.($DT->{rankingcount}+0).l("回")." ".GetTopCountImage($DT->{rankingcount}+0).$TRE;
	$disp.=$GUILD{$DT->{guild}} ? $TDB.l('ギルド会費')."<br><SMALL>(".l('決算時徴収').")</SMALL><td colspan=2>$term[0]".int($DT->{saletoday}*$GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/1000)."$term[1]"."<SMALL>/".l('売上の').($GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/10)."%</SMALL>" : $TD."　<td colspan=2>　";
	$disp.=$TRE.$TBE;
}
else
{
	$disp.=l('名前').':'.$DT->{name}."<BR>";
	$disp.=l('店名').':'.GetTagImgGuild($DT->{guild}).$DT->{shopname}."<BR>";
	$disp.=l('RANK').':'.($id2idx{$DT->{id}}+1)."<BR>";
	$disp.=l('人気').':'.$rankmsg."<BR>";
	$disp.=l('ごみ').':'.GetCleanMessage($DT->{trush})."<BR>";
	$disp.=l('資金').':'.GetMoneyString($DT->{money})."<BR>";
	$disp.=l('今売').':'.GetMoneyString($DT->{saletoday})."<BR>";
	$disp.=l('今払').':'.GetMoneyString($DT->{paytoday})."<BR>";
	$disp.=l('今維').':'.GetMoneyString(int($DT->{costtoday}))."+".GetMoneyString($SHOWCASE_COST[$DT->{showcasecount}-1])."<BR>";
	$disp.=l('時間').':'.$tm."<BR>";
	$disp.=l('点数').':'.$DT->{point}."<BR>";
	$disp.=l('職業').':'.$job."<BR>";
}
1;
