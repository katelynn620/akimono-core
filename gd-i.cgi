# �M���h�T�㎺ 2004/01/20 �R��

$NOITEM=1;
DataRead();
CheckUserPass(1);
OutError('�M���h�ɓ����Ă��܂���') if !$DT->{guild};
RequireFile('inc-gd.cgi');

my $lv=int( $GUILD_DATA{$DT->{guild}}->{money} / 111000);
$lv = 1 if ( $lv < 1 ) ;
$lv = 200 if ( $lv > 200 ) ;

$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>�M���h��t</SPAN>�F".GetTagImgGuild($DT->{guild});
$disp.="<BIG>".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."</BIG>�����W�������ł��B<br>";
$disp.="���݂̏����W���x����".$lv."�ł��B".$TRE.$TBE."<br>";

	undef @MESSAGE;

		open(IN,GetPath("log0"));
		push(@MESSAGE,<IN>);
		close(IN);
		open(IN,GetPath("log1"));
		push(@MESSAGE,<IN>);
		close(IN);

		my $id=0;
		
		@MESSAGE=grep(/^\d+\t\d+\t(\d+\d)\t/o,@MESSAGE);
		@MESSAGE=("0,0,0,���͂���܂���\n") if !scalar(@MESSAGE);

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
		$disp.="<small>".GetTime2FormatTime($tm)."</small> <SPAN>".$DT[$id2idx{$id}]->{shopname}."</SPAN>�F".$message;}
		else	{
		$disp.="<small>".GetTime2FormatTime($tm)."</small> <SPAN>�H�H�H�H�H�H</SPAN>�F".$message;}
	
	$disp.="<BR>";
	}
$disp.="</td></tr></table>";
$disp.=$pagecontrol;

OutSkin();
1;
