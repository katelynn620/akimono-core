# ÉMÉãÉhè⁄ç◊ 2004/01/20 óRò“

DataRead();
CheckUserPass(1);
RequireFile('inc-gd.cgi');

undef @guildDT;
my $Gcount=0;
my $idx=-1;
foreach(@DT)
{
	$idx++;
	next if ($_->{guild} ne $Q{g});
	$guildDT[$Gcount]=$_;
	$guildDT[$Gcount]->{count}=$idx;	#èáà èÓïÒÇéÊìæÇµÇƒÇ®Ç≠
	$Gcount++;
}

my ($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$RANKING_PAGE_ROWS,$Gcount);

ReadLetterName();
my $lt=$GUILD_DETAIL{$Q{g}}->{leadt};
my $staff=$GUILD_DETAIL{$Q{g}}->{$MYDIR};

$disp.="<table width=520>";
$disp.=$TR.$TDB.'ê≥éÆñºèÃ'.$TD."<b>".GetTagImgGuild($Q{g}).$GUILD_DETAIL{$Q{g}}->{name}."</b>";
if ($GUILD_DETAIL{$Q{g}}->{url})
	{$disp.=qq| <a target="_blank" href="action.cgi?key=jump&guild=$Q{g}">[HP]</a>|;}
$disp.=$TRE;
$disp.=$TR.$TDB.'ící∑'.$TD.SearchLetterName($GUILD_DETAIL{$Q{g}}->{leader},$lt)." ($Tname{$lt})".$TRE;
$disp.=$TR.$TDB.'äXÇÃåRét'.$TD.(defined($id2idx{$staff}) ? $DT[$id2idx{$staff}]->{shopname} : "ïsç›").$TRE;
$disp.=$TR.$TDB.'äàìÆè–âÓ'.$TD.$GUILD_DETAIL{$Q{g}}->{appeal}.$TRE;
$disp.=$TR.$TDB.'ì¸ícèåè'.$TD.$GUILD_DETAIL{$Q{g}}->{needed}.$TRE;
$disp.=$TBE;

my $pagecontrol=GetPageControl($pageprev,$pagenext,"g=".$Q{g},"",$pagemax,$page);
$disp.=$pagecontrol."<BR>";

$disp.=$TB;

	$disp.=$TR;
	$disp.=$TDB."ì_êî";
	$disp.=$TDB."ìXí∑";
	$disp.=$TDB."ÉWÉáÉu";
	$disp.=$TDB."å®èëÇ´Å@ìXñº";
	$disp.=$TDB."è§ïi Åyënã∆Åz ÉRÉÅÉìÉg";
	$disp.=$TRE;

foreach my $idx ($pagestart..$pageend)
{
	my $DT=$guildDT[$idx];
	my $rankupdown="(êV)";
	if($DT->{rankingyesterday})
	{
		$rankupdown=$DT->{rankingyesterday}-$DT->{count}-1;
		$rankupdown=$rankupdown==0 ? " Å® ": $rankupdown<0 ? "Å´".(-$rankupdown) : "Å™".$rankupdown;
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
	
	$disp.=$TR;
	$disp.="<td align=right><b>No.".($DT->{count}+1)."</b>".$rankupdown;
	$disp.="<br>".$DT->{point};
	$disp.=$TDNW.$tdh_pt.GetTagImgKao($DT->{name},$DT->{icon});
	$disp.="<td align=center>".GetTagImgJob($DT->{job},$DT->{icon});
	$disp.=$TD.$tdh_nm;
	$disp.="<SPAN>".$DT->{user}{_so_e}."</SPAN><br>" if ($DT->{user}{_so_e} ne '');
	$disp.=    "<a href=\"action.cgi?key=shop-b&ds=$DT->{id}&$USERPASSURL\">" if !$GUEST_USER;
	$disp.=    GetTagImgGuild($DT->{guild}).$job.$DT->{shopname};
	$disp.=    "</a>" if !$GUEST_USER;
	$disp.=GetTopCountImage($DT->{rankingcount}+0) if $DT->{rankingcount};
	$disp.=DignityDefine($DT->{dignity},1);
	
	$disp.=$TD.$tdh_sc.$itempro.$salelist."<BR>";
	$disp.=$tdh_fd."Åy".GetTime2found($NOW_TIME-$DT->{foundation})."Åz";
	$disp.=$tdh_cm.$DT->{comment} if $DT->{comment};
	$disp.=$TRE;
}
$disp.=$TBE;
$disp.=$pagecontrol;

OutSkin();
1;
