use utf8;
# 入賞リスト表示 2005/01/06 由來

$disp.="<BIG>●".l('新聞：入賞リスト')."</BIG><br><br>";
$disp.=$TB.$TR;

	@DT=sort{$b->{rankingcount}<=>$a->{rankingcount}}@DT;

$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>".l('最多優勝')."</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>".l('優勝回数')."<br>".($DT[0]->{rankingcount}+0).l("回");
$disp.="<td>".$DT[0]->{comment};

	@DT=sort{$b->{taxyesterday}<=>$a->{taxyesterday}}@DT;

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>".l('納税トップ')."</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>".l('前期納税金')."<br>".GetMoneyString($DT[0]->{taxyesterday});
$disp.="<td>".$DT[0]->{comment};

	@DT=sort{$b->{money}<=>$a->{money}}@DT;

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>".l('大富豪')."</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>".l('資金')."<br>".GetMoneyString($DT[0]->{money});
$disp.="<td>".$DT[0]->{comment};

	@DT=reverse(@DT);

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>".l('貧乏ヒマなし')."</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>".l('資金')."<br>".GetMoneyString($DT[0]->{money});
$disp.="<td>".$DT[0]->{comment};

	@DT=sort{$b->{costyesterday}<=>$a->{costyesterday}}@DT;

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>".l('維持費かかりすぎ')."</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>".l('前期維持費')."<br>".GetMoneyString($DT[0]->{costyesterday});
$disp.="<td>".$DT[0]->{comment};

	@DT=sort{$b->{trush}<=>$a->{trush}}@DT;

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>".l('掃除サボりすぎ')."</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>".l('ごみ')."<br>".GetCleanMessage($DT[0]->{trush});
$disp.="<td>".$DT[0]->{comment};

	@DT=sort{$b->{rank}<=>$a->{rank}}@DT;

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>".l('ただいま大人気')."</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>".l('人気')."<br>".GetRankMessage($DT[0]->{rank});
$disp.="<td>".$DT[0]->{comment};

	@DT=reverse(@DT);

$disp.=$TRE.$TR;
$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT[0]->{name},$DT[0]->{icon});
$disp.=$TD."<SPAN>".l('お客さん来てぇ')."</SPAN><br><b>".$DT[0]->{shopname}."</b>";
$disp.="<td>".l('人気')."<br>".GetRankMessage($DT[0]->{rank});
$disp.="<td>".$DT[0]->{comment};

$disp.="</td></tr></table>";
1;
