use utf8;
# ギルド探偵室 2004/01/20 由來

$NOITEM=1;
DataRead();
CheckUserPass(1);
OutError(l('ギルドに入っていません')) if !$DT->{guild};
RequireFile('inc-gd.cgi');

my $lv=int( $GUILD_DATA{$DT->{guild}}->{money} / 111000);
$lv = 1 if ( $lv < 1 ) ;
$lv = 200 if ( $lv > 200 ) ;

$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>".l('ギルド受付')."</SPAN>：".GetTagImgGuild($DT->{guild});
$disp.=l("<BIG>%1</BIG>が収集した情報です。",$GUILD{$DT->{guild}}->[$GUILDIDX_name])."<br>";
$disp.=l("現在の情報収集レベルは%1です。",$lv).$TRE.$TBE."<br>";

	undef @MESSAGE;

		open(IN,"<:encoding(UTF-8)",GetPath("log0"));
		push(@MESSAGE,<IN>);
		close(IN);
		open(IN,"<:encoding(UTF-8)",GetPath("log1"));
		push(@MESSAGE,<IN>);
		close(IN);

		my $id=0;
		
		@MESSAGE=grep(/^\d+\t\d+\t(\d+\d)\t/o,@MESSAGE);
		@MESSAGE=("0,0,0,".l('情報はありません')."\n") if !scalar(@MESSAGE);

$lv = scalar(@MESSAGE) if ( $lv > scalar(@MESSAGE) ) ;

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax);
my $pagecontrol="";

	($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{lpg},$LIST_PAGE_ROWS,$lv);
	

	$pagecontrol=GetPageControl($pageprev,$pagenext,"cmd=info","lpg",$pagemax,$page);
	$disp.=$pagecontrol;
	
	$disp.="<BR>";


$disp.="<table><tr><td>";
foreach my $cnt ($pagestart..$pageend)
	{
	my $msg=$MESSAGE[$cnt];
	next if $msg eq '';
	my($tm,$mode,$id,$message)=split('\t',$msg);
	chop($message);

		if ($lv > 20 && defined($id2idx{$id}))	{
		$disp.="<small>".GetTime2FormatTime($tm)."</small> <SPAN>".$DT[$id2idx{$id}]->{shopname}."</SPAN>：".$message;}
		else	{
		$disp.="<small>".GetTime2FormatTime($tm)."</small> <SPAN>".l('？？？？？？')."</SPAN>：".$message;}
	
	$disp.="<BR>";
	}
$disp.="</td></tr></table>";
$disp.=$pagecontrol;

OutSkin();
1;
