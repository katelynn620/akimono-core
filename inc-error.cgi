# �G���[���͂ƈ��S�ȏI�� 2005/03/30 �R��

my($msg)=@_;
die($msg) if $ERROR_REENTRY;	# ���[�v�h�~
$ERROR_REENTRY=1;

@_=(gmtime(time()+60*60*9))[5,4,3,2,1,0];
$_[0]+=1900; $_[1]++;
my $nowtime=sprintf("%d/%02d/%02d %02d:%02d:%02d",@_);

	open(OUT,">>$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT");
	print OUT "1";
	close(OUT);
	
my $er_m="���͂ł��܂���ł����B";

$msg=~s/&/&amp;/g;
$msg=~s/"/&quot;/g;
$msg=~s/</&lt;/g;
$msg=~s/>/&gt;/g;
$msg=~s/\n/<br>/g;
if ($msg =~ /at\s(\S+)\sline/) {
	$er_s=$1;
	$er_sm="";
	$er_sm="<br>���̃t�@�C������ɉ��ς��Ă��Ȃ��ꍇ�͕ʂȃt�@�C���ɃG���[������܂��B" if ($msg =~ /func/);
	$er_sm="<br>����́u<b>inc-item-data.cgi</b>�v���C�����邱�Ƃɂ��������܂��B" if ($msg =~ /data\/item/);
}
if ($msg =~ /line\s(\d+)[,\.]/) {
	$er_l=$1;
}
if ($msg =~ /syntax\serror/ || $msg =~ /Scalar\sfound/ || $msg =~ /Array\sfound/) {
	$er_m="���@�~�X�ł��B�u\"�v�u\'�v�u\;�v�u\}�v�Ȃǂ̂��Y��ł��邱�Ƃ������ł��B";
}
if ($msg =~ /Unrecognized\scharacter/) {
	$er_m="�����ł��Ȃ��������܂܂�Ă��܂��B�ԈႦ�đS�p�������g���Ă��܂������C<br>�S�p�������u\"�v��u\'�v�Ȃǂł�����̂�Y��Ă��邱�Ƃ������ł��B";
}
if ($msg =~ /Illegal\sdivision\sby\szero/) {
	$er_m="�[���Ŋ���v�Z�������Ă��܂��B<br>����ϐ��Ŋ���Ƃ��ɂ́C���̕ϐ����[���ɂȂ�ꍇ�͌v�Z��������Ă��������B";
}
if ($msg =~ /Can't\sfind\sstring\sterminator/) {
	$er_m="�����񂪁u\"�v��u\'�v�Ȃǂŕ����Ă��܂���B";
}
if ($msg =~ /Unmatched\sright/) {
	$er_m="���@�~�X�ł��B�u\}�v��u)�v�Ȃǂ��]�v�ɑ����悤�ł��B";
}
if ($msg =~ /Missing\sright/) {
	$er_m="���@�~�X�ł��B�u\}�v��u)�v�Ȃǂ����Y��Ă���悤�ł��B";
}
if ($msg =~ /not\sdefined\sfunction/) {
	$er_m="�T�u���[�`���̖��̂Ƀ~�X������悤�ł��B<br>�����Ƃ��ẮC�o�[�W�����A�b�v�̃~�X�C�A�C�e���f�[�^�̃C�x���g�֘A�̃~�X�Ȃǂ��l�����܂��B";
}
if ($msg =~ /Can't\slocate/) {
	$er_m="�t�@�C�������݂��܂���B�C�x���g��A�C�e���f�[�^���폜�������߂�������܂���B";
}

PrintErr();

my $error_count=(-s "$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT");
if ($error_count > 9)
{
	mkdir("$DATA_DIR/lock",$DIR_PERMISSION) unless (-d "$DATA_DIR/lock")
}

UnLock() if $LOCKED;	#���b�N����
CoUnLock() if $COLOCKED;
exit(-1);
1;


sub PrintErr
{
print "Cache-Control: no-cache, no-store\n";
print "Pragma: no-cache\n";
print "Content-type: text/html; charset=Shift_JIS\n\n";
print <<"STR";
<HTML><HEAD>
<Style Type="text/css">
<!--
A:link   { font-weight: bold; text-decoration:none}
A:visited{ font-weight: bold; text-decoration:none}
A:hover  { font-weight: bold; text-decoration:underline;}
BODY,TR,TD,TH { font-family:"MS UI Gothic"; font-size:11pt; }
SPAN { font-family:"Comic Sans MS"; font-size:16pt; color:#664499 ;}
input,input.button{color:#000000;background-color:#FFFFFF;border:1 #5f5f8c solid}
-->
</Style>
<TITLE>$HTML_TITLE:�G���[</TITLE>
</HEAD>
<BODY BGCOLOR="#FFFFFF" TEXT="#000000" LINK="#6050cc" VLINK="#6050cc" ALINK="#FF0000">
<center><br><SPAN>Sorry, An Error is Detected.</SPAN><br><br>
<TABLE cellspacing="0" cellpadding="0"><TBODY><TR><TD bgcolor="#6B6599">
<TABLE cellspacing="1" cellpadding="0" border="0" width="700"><TBODY><TR><TD bgcolor="#FFFFFF" align="center">
<br>�G���[���������ꂽ���߁C���s�����~����܂����B<br><br>
�v���C���̕��ɂ͂��s�ւ����������܂����C�����܂ł��΂炭���҂����������B<br>
�Ȃ��Ȃ��������Ȃ��ꍇ�́C���萔�ł���<a href="mailto:$ADMIN_EMAIL">�Ǘ��l�܂ł��A��</a>���������B<br><br>
<A HREF=\"$HOME_PAGE\" TARGET=_top>[�z�[���ɖ߂�]</A>
<br><div align="right"><small>
<A HREF="http://akimono.org//">���l����</A></small></div>
</TD></TR></TBODY></TABLE>
</TD></TR></TBODY></TABLE>
<br><TABLE cellspacing="0" cellpadding="1" border="0">
<TBODY><TR vAlign=center align=middle><TD bgcolor="#6B6599">
<TABLE cellspacing="0" cellpadding="5" width="700" border="0">
<TBODY><TR><TD width="80" bgcolor="#ABA5FF" align="center">
<FONT color="#FFFFFF"><small>for Admin</small></FONT></TD>
<TD align="center" bgcolor="#DBD5FF">�ȉ��̃A�h�o�C�X�ɏ]���ăG���[���������Ă��������B �c 
<A HREF="http://akimono.org/">[�G���[���k]</A>
</TD></TR></TBODY></TABLE></TD></TR></TBODY></TABLE>
<br><TABLE cellspacing="0" cellpadding="5" width="700" border="0">
<TR><TD width="80" bgcolor="#ABA5FF" align="center">
<FONT color="#FFFFFF"><small>�G���[��</small></FONT></TD>
<td bgcolor="#DBD5FF">$MYNAME �̎��s�ɂ�蔭���B<small>($nowtime)</small></tr>
<TR><TD width="80" bgcolor="#ABA5FF" align="center">
<FONT color="#FFFFFF"><small>�G���[����</small></FONT></TD>
<td bgcolor="#DBD5FF">�u<b>$er_s</b>�v�� $er_l�s�ڕt�߂Ɍ���������悤�ł��B$er_sm</tr>
<TR><TD width="80" bgcolor="#ABA5FF" align="center">
<FONT color="#FFFFFF"><small>�G���[����</small></FONT></TD>
<td bgcolor="#DBD5FF">$er_m</tr>
<TR><TD width="80" bgcolor="#ABA5FF" align="center">
<FONT color="#FFFFFF"><small>Error Data</small></FONT></TD>
<td bgcolor="#DBD5FF"><small>$msg</small></tr></table>
</CENTER><br><div align="right">
<FORM ACTION="admin.cgi" METHOD="POST"><INPUT TYPE=PASSWORD size=6 NAME=admin>
<INPUT TYPE=SUBMIT VALUE="Admin"></FORM></div>
</body></html>
STR

my $txt= <<"STR";
$MYNAME �̎��s�ɂ�蔭���B($nowtime)
�u$er_s�v�� $er_l�s�ڕt�߂Ɍ���������悤�ł��B$er_sm
$er_m
$msg
STR

	my $ErrFile = $DATA_DIR."/error.log";
	open(OUT,"> $ErrFile");
	print OUT $txt;
	close(OUT);
	chmod (0666,$ErrFile);
}

