# �V���i���ʁj 2005/01/06 �R��

my ($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$RANKING_PAGE_ROWS,$DTusercount);

$disp.="<BIG>���V���F���ʃ��X�g</BIG><br><br>";
my $pagecontrol=GetPageControl($pageprev,$pagenext,"t=4","",$pagemax,$page);
$disp.=$pagecontrol."<BR>";
$disp.=$TB;

if(!$MOBILE)
{
	$disp.=$TR;
	$disp.=$TDB."�_��";
	$disp.=$TDB."�X��";
	$disp.=$TDB."�W���u";
	$disp.=$TDB."�X���@�l�C";
	$disp.=$TDB."��������";
	$disp.=$TDB."����";
	$disp.=$TDB."�n��";
	$disp.=$TDB."���i �y�n�Ɓz �R�����g";
	$disp.=$TRE;
}
else
{
	$tdh_rk="RANK:";
	$tdh_pt="�_��:";
	$tdh_nm="�X��:";
	$tdh_pp="�l�C:";
	$tdh_mo="����:";
	$tdh_ts="�{��:";
	$tdh_ys="��:";
	$tdh_cs="�ێ�:";
	$tdh_sc="�ꉟ:";
	$tdh_cm="�ꌾ:";
	$tdh_tx="���:";
	$tdh_ex="�n��:";
	$tdh_fd="�n��:";
}

foreach my $idx ($pagestart..$pageend)
{
	my $DT=$DT[$idx];
	
	my $rankupdown="(�V)";
	if($DT->{rankingyesterday})
	{
		$rankupdown=$DT->{rankingyesterday}-$idx-1;
		$rankupdown=$rankupdown==0 ? " �� ": $rankupdown<0 ? "��".(-$rankupdown) : "��".$rankupdown;
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
	$disp.=    "<a href=\"action.cgi?key=shop-b&ds=$DT->{id}&$USERPASSURL\">" if !$GUEST_USER;
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
	
	$disp.=$tdh_fd."�y".GetTime2found($NOW_TIME-$DT->{foundation})."�z";
	$disp.=$tdh_cm.$DT->{comment} if $DT->{comment};
	$disp.=$TRE;
}
$disp.=$TBE;

$disp.=$pagecontrol;
1;
