# �h���S�����[�X �����X�|�\�� 2005/03/30 �R��

$disp.="<BIG>���h���S�����[�X�F�����X�|</BIG><br><br>";
$disp.="$TB$TR$TD".GetTagImgKao("�ҏW��","slime4").$TD;
$disp.="<SPAN>�ҏW��</SPAN>�F������ǃX�|�[�c�V���ł́C�����ɖ𗧂���񋟂��Ă���B<br>";
$disp.="�{�^���������ƕʃE�C���h�E�ŊJ���̂ŁC�����Q�Ƃ��Ȃ��瑀��ł���񂾁B".$TRE.$TBE;
$disp.=<<STR;
<br><FORM>
<input type="button" value="�X�P�W���[��" onclick="javascript:window.open('action.cgi?key=slime-l&mode=sche','_blank','width=760,height=580,scrollbars')">
<input type="button" value="�������ꗗ" onclick="javascript:window.open('action.cgi?key=slime-l&mode=dra','_blank','width=760,height=580,scrollbars')">
<input type="button" value="�B�����ꗗ" onclick="javascript:window.open('action.cgi?key=slime-l&mode=pr','_blank','width=760,height=580,scrollbars')">
<input type="button" value="�q��ꗗ" onclick="javascript:window.open('action.cgi?key=slime-l&mode=rc','_blank','width=760,height=580,scrollbars')">
<input type="button" value="�X�Ɉꗗ" onclick="javascript:window.open('action.cgi?key=slime-l&mode=st','_blank','width=760,height=580,scrollbars')">
<input type="button" value="�R��ꗗ" onclick="javascript:window.open('action.cgi?key=slime-l&mode=jk','_blank','width=760,height=580,scrollbars')">
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
	{$disp.="<small>".GetTime2FormatTime($tm)."</small> <SPAN>[�o��]".$message."</SPAN>";}
	elsif ($mode==2)
	{$disp.="<small>".GetTime2FormatTime($tm)."</small> <BIG>[�d��]".$message."</BIG>";}
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
	open(IN,GetPath($COMMON_DIR,"dra-log0"));
	push(@MESSAGE,<IN>);
	close(IN);
	open(IN,GetPath($COMMON_DIR,"dra-log1"));
	push(@MESSAGE,<IN>);
	close(IN);
	@MESSAGE=("0\t0\t���͂���܂���\n") if !scalar(@MESSAGE);
}

