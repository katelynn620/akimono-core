# ãÊ\¦ 2005/01/06 RÒ

my ($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$TOP_RANKING_PAGE_ROWS,$DTusercount);

$disp.="<BIG>gbv $TOP_RANKING_PAGE_ROWSÌXÜ</BIG>F".GetMenuTag('log','[Ú×]','&t=4')."<br><br>";
$disp.=$TB;

	$disp.=$TR;
	$disp.=$TDB."_";
	$disp.=$TDB."X·";
	$disp.=$TDB."Wu";
	$disp.=$TDB."X¼@lC";
	$disp.=$TDB."¡úã";
	$disp.=$TDB."à";
	$disp.=$TDB."nû";
	$disp.=$TDB."¤i ynÆz Rg";
	$disp.=$TRE;

foreach my $idx ($pagestart..$pageend)
{
	my $DT=$DT[$idx];
	
	my $rankupdown="(V)";
	if($DT->{rankingyesterday})
	{
		$rankupdown=$DT->{rankingyesterday}-$idx-1;
		$rankupdown=$rankupdown==0 ? " ¨ ": $rankupdown<0 ? "«".(-$rankupdown) : "ª".$rankupdown;
		$rankupdown="<small>($rankupdown)</small>";
	}
	my $itemtype=-1;
	my $itempro="";
	my $salelist="";
	foreach(0..$DT->{showcasecount}-1)
	{
		my $no=$DT->{showcase}[$_];
		$salelist.=GetTagImgItemType($no);
		$itemtype=0,next if $itemtype!=-1 && $ITEM[$no]->{type}!=$itemtype;
		$itemtype=$ITEM[$no]->{type};
	}
	$itempro=GetTagImgItemType(0,$itemtype,1)." " if $itemtype;
	my $itemno=$DT->{showcase}[0];
	$salelist.=" ".$ITEM[$itemno]->{name}." ".GetMoneyString($DT->{price}[0]) if $itemno;
	
	my $expsum=0;
	foreach(values(%{$DT->{exp}})){$expsum+=$_;}
	$expsum=int($expsum/10)."%";
	
	$disp.=$TR;
	$disp.="<td align=right><b>No.".($idx+1)."</b>".$rankupdown;
	$disp.="<br>".$DT->{point};
	$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT->{name},$DT->{icon});
	$disp.="<td align=center>".GetTagImgJob($DT->{job},$DT->{icon});
	$disp.=$TD.$tdh_nm;
	$disp.=    "<a href=\"shop.cgi?ds=$DT->{id}&$USERPASSURL\">" if !$GUEST_USER;
	$disp.=    GetTagImgGuild($DT->{guild}).$job.$DT->{shopname};
	$disp.=    "</a>" if !$GUEST_USER;
	$disp.=GetTopCountImage($DT->{rankingcount}+0) if $DT->{rankingcount};
	$disp.="<BR>";
	$disp.=GetRankMessage($DT->{rank});
	$disp.=$TDNW.$tdh_ts.GetMoneyString($DT->{saletoday});
	$disp.=$TDNW.$tdh_mo.GetMoneyMessage($DT->{money});
	$disp.=$TDNW.$tdh_ex.$expsum;
	
	$disp.=$TD;
	
	$disp.=$tdh_sc.$itempro.$salelist;
	
	$disp.="<BR>";
	
	$disp.=$tdh_fd."y".GetTime2found($NOW_TIME-$DT->{foundation})."z";
	$disp.=$tdh_cm.$DT->{comment} if $DT->{comment};
	$disp.=$TRE;
}
$disp.=$TBE;
1;
