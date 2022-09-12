use utf8;
# 新聞下請け 2003/07/19 由來

my $topic=$Q{key} ne "log";

$disp.=$topic ? "<BIG>" . l('%1の出来事',$DT->{shopname}). "</BIG><br><br>" : "<BIG>".l('●新聞：速報')."</BIG><br><br>";

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax);
my $pagecontrol="";

if($topic)
{
	($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)=(0,0,$MAIN_LOG_PAGE_ROWS-1,0,0,0);
}
else
{
	($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{lpg},$LIST_PAGE_ROWS,scalar(@MESSAGE));
	
	my $formtarget="<OPTION VALUE=\"\"".($Q{tgt}eq""?" SELECTED":"").">".l("全");
	foreach (@DT)
	{
		my $name=$_->{shopname};
		$formtarget.="<OPTION".($name eq $Q{tgt}?' SELECTED':'').">$name";
	}
	my $formmode="";
	foreach (0..3)
	{
		my $name=(l('全'),l('重要'),l('情報'),l('行動'))[$_];
		$formmode.="<OPTION VALUE=\"$_\"".($Q{lmd}==$_?" SELECTED":"").">$name";
	}
	
	$disp.=<<"HTML";
<form action="action.cgi" $METHOD>
<input type=hidden name=lpg value="0">
$MYFORM$USERPASSFORM
<select name=tgt>
$formtarget
</select>
<input type=text name=kw value="$Q{kw}">
<select name=lmd>
$formmode
</select>
HTML
	$disp.= '<input type=submit value="'.l('検索').'">
</form>';


	my $key=$Q{kw};
	$key=~s/(\W)/'%'.unpack('H2',$1)/eg;
	my $tgt=$Q{tgt};
	$tgt=~s/(\W)/'%'.unpack('H2',$1)/eg;

	my $search="";
	$search.="&kw=".$key if $key ne '';
	$search.="&tgt=".$tgt if $tgt ne '';
	$search.="&lmd=".($Q{lmd}+0) if $Q{lmd};

	$pagecontrol=GetPageControl($pageprev,$pagenext,$search,"lpg",$pagemax,$page);
	$disp.=$pagecontrol;
	
	$disp.="<BR>";
}

$disp.=$TB;
if (!$topic && @EVENTMSG) {
	foreach (sort(@EVENTMSG))
		{$disp.=$TR.$TDB.l('情報').'：'.$_.$TRE;}
	}
$disp.=$TR.$TD;
foreach my $cnt ($pagestart..$pageend)
{
	my $msg=$MESSAGE[$cnt];
	next if $msg eq '';
	my($tm,$mode,$id,$message)=split('\t',$msg);
	chop($message);
	
	if($MOBILE)
	{
		if($id==$DT->{id})
			{$disp.=l("秘").":".$message;}
		elsif($mode==1)
			{$disp.="★".l('重要').":".$message;}
		elsif($mode==2)
			{$disp.="●".l('情報').":".$message;}
		elsif($mode==3)
			{$disp.="○".l('行動').":".$message;}
		else
			{$disp.=$message;}
	}
	else
	{
		if($id==$DT->{id})
			{$disp.="<FONT COLOR=\"#666666\">".$message."(".l('秘').")</FONT>";}
		elsif($mode==1)
			{$disp.="<small>".GetTime2FormatTime($tm)."</small> <BIG>[".l('重要')."]".$message."</BIG>";}
		elsif($mode==2)
			{$disp.="<small>".GetTime2FormatTime($tm)."</small> <SPAN>[".l('情報')."]".$message."</SPAN>";}
		elsif($mode==3)
			{$disp.="<small>".GetTime2FormatTime($tm)."</small> [".l('行動')."]<B>".$message."</B>";}
		else
			{$disp.="<small>".GetTime2FormatTime($tm)."</small> ".$message;}
	}
	
	$disp.="<BR>";
}

$disp.=$TRE.$TBE;

$disp.=$pagecontrol;

1;
