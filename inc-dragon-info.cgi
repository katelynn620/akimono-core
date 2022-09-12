use utf8;
# ドラゴンレース あきスポ表示 2005/03/30 由來

$disp.="<BIG>●".l('ドラゴンレース')."：".l('あきスポ')."</BIG><br><br>";
$disp.="$TB$TR$TD".GetTagImgKao(l("編集長"),"slime4").$TD;
$disp.="<SPAN>".l('編集長')."</SPAN>：".l('あきんどスポーツ新聞では，競竜に役立つ情報を提供している。')."<br>";
$disp.=l("ボタンを押すと別ウインドウで開くので，情報を参照しながら操作できるんだ。").$TRE.$TBE;
$disp.=<<STR;
<br><FORM>
<input type="button" value="${\l('スケジュール')}" onclick="javascript:window.open('action.cgi?key=slime-l&mode=sche','_blank','width=760,height=580,scrollbars')">
<input type="button" value="${\l('競争竜一覧')}" onclick="javascript:window.open('action.cgi?key=slime-l&mode=dra','_blank','width=760,height=580,scrollbars')">
<input type="button" value="${\l('隠居竜一覧')}" onclick="javascript:window.open('action.cgi?key=slime-l&mode=pr','_blank','width=760,height=580,scrollbars')">
<input type="button" value="${\l('牧場一覧')}" onclick="javascript:window.open('action.cgi?key=slime-l&mode=rc','_blank','width=760,height=580,scrollbars')">
<input type="button" value="${\l('厩舎一覧')}" onclick="javascript:window.open('action.cgi?key=slime-l&mode=st','_blank','width=760,height=580,scrollbars')">
<input type="button" value="${\l('騎手一覧')}" onclick="javascript:window.open('action.cgi?key=slime-l&mode=jk','_blank','width=760,height=580,scrollbars')">
</FORM>
STR
ReadDraLog();

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax);
my $pagecontrol="";
($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{lpg},$LIST_PAGE_ROWS,scalar(@MESSAGE));
	
	$pagecontrol=GetPageControl($pageprev,$pagenext,"mode=info","lpg",$pagemax,$page);
	$disp.=$pagecontrol;
	
	$disp.="<BR>";

$disp.=$TB;
$disp.=$TR.$TD;
foreach my $cnt ($pagestart..$pageend)
{
	my $msg=$MESSAGE[$cnt];
	next if $msg eq '';
	my($tm,$mode,$message)=split('\t',$msg);
	chop($message);

	if ($mode==1)
	{$disp.="<small>".GetTime2FormatTime($tm)."</small> <SPAN>[".l('登竜')."]".$message."</SPAN>";}
	elsif ($mode==2)
	{$disp.="<small>".GetTime2FormatTime($tm)."</small> <BIG>[".l('重賞')."]".$message."</BIG>";}
	else
	{$disp.="<small>".GetTime2FormatTime($tm)."</small> ".$message;}
	$disp.="<BR>";
}
$disp.=$TRE.$TBE;
$disp.=$pagecontrol;
1;

sub ReadDraLog
{
	undef @MESSAGE;
	open(IN,"<:encoding(UTF-8)",GetPath($COMMON_DIR,"dra-log0"));
	push(@MESSAGE,<IN>);
	close(IN);
	open(IN,"<:encoding(UTF-8)",GetPath($COMMON_DIR,"dra-log1"));
	push(@MESSAGE,<IN>);
	close(IN);
	@MESSAGE=("0\t0\t".l('情報はありません')."\n") if !scalar(@MESSAGE);
}

