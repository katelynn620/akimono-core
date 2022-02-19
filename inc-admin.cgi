# �Ǘ�����ʉ����� 2003/09/25 �R��

if(-e "$DATA_DIR/$LASTTIME_FILE$FILE_EXT")
	{
		push(@log,'���݃����e���[�h�ɂ��C�Q�[���̐i�s���~�܂��Ă��܂��B') if -e "./lock" or -e "$DATA_DIR/lock";
		push(@log,'�Q�[���f�[�^���Ȃ��Ȃ��Ă��܂��B'," �o�b�N�A�b�v�𕜌����邩���������K�v�ł��B") if !-e "$DATA_DIR/$DATA_FILE$FILE_EXT";
		my $init=' �������{�^���i���j���[�����j�������ďC�����Ă��������B';
		push(@log,'�M���h��`�t�@�C�����Ȃ��Ȃ��Ă��܂��B',$init) if !-e "$DATA_DIR/$GUILD_FILE$FILE_EXT";
		push(@log,'���b�N�t�@�C�����Ȃ��Ȃ��Ă��܂��B',$init) if !GetFileList($DATA_DIR,"^$LOCK_FILE");
		push(@log,'���L���b�N�t�@�C�����Ȃ��Ȃ��Ă��܂��B',$init) if !GetFileList($COMMON_DIR,"^$LOCK_FILE");
		foreach my $dir ($SESSION_DIR,$TEMP_DIR,$COTEMP_DIR,$LOG_DIR,$SUBDATA_DIR,$BACKUP_DIR)
		{
			push(@log,$dir.' ���Ȃ��Ȃ��Ă��܂��B',$init) if !-e $dir;
		}
		push(@log,' ���i�f�[�^���쐬���Ă��������B') if !-e $ITEM_DIR;
	}
	else
	{
		push(@log,' ���������s���Ă��������i���j���[�����j');
	}
	
if(-e "$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT")
	{
	my $errorcount=(-s "$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT")+0;
	unlink("$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT");
	push(@log,'�O��̊Ǘ����猻�݂܂� '.$errorcount.'��̃G���[�����m���܂����B');
	}
	push(@log,"<A HREF=\"$DATA_DIR/error.log\">[�G���[���]</A> ���񍐂���Ă��܂��B") if(-e "$DATA_DIR/error.log");
	
	my $backupselect=qq|<option value="" selected>�o�b�N�A�b�v��I��|;
	my $backupbasedir=$BACKUP_DIR;
	$backupbasedir=~s/\/([^\/]*)$//;
	foreach(GetFileList($backupbasedir,"^$1"))
	{
		my $file=$_;
		my $time=(stat("$file/$DATA_FILE$FILE_EXT"))[9];
		next if !$time;
		my($s,$min,$h,$d,$m,$y)=gmtime($time+$TZ_JST);
		my $timestr=sprintf("%04d-%02d-%02d %02d:%02d",$y+1900,$m+1,$d,$h,$min);
		$backupselect.=qq|<option value="$_">$timestr|;
	}
	
	my $userselect=qq|<option value="" selected>���[�U�[��I��|;
if(open(IN,"$DATA_DIR/$DATA_FILE$FILE_EXT"))
	{
		while(<IN>){s/[\r\n]//g; last if $_ eq '//';}
		my @data=<IN>;
		close(IN);
		if(scalar(@data))
		{
			for(my $idx=0; $idx<$#data; $idx+=2)
			{
				@_=split(/,/,$data[$idx],5);
				
				$userselect.=qq|<option value="$_[2]">$_[2] : $_[3]|;
			}
		}
	}
	eval {
	require "$ITEM_DIR/item.cgi" if -e "$ITEM_DIR/item.cgi";
	};
	if ($@)
	{
	push(@log,' inc-item-data.cgi�ɃG���[������C�f�[�^���擾�ł��܂���B');
	push(@log,'�ꕔ�̊Ǘ��@�\������ɓ��삵�Ȃ��\��������܂��B');
	}
	else
	{
	foreach(1..$MAX_ITEM){$sort[$_]=$ITEM[$_]->{sort}};
	my @itemlist=sort { $sort[$a] <=> $sort[$b] } (1..$MAX_ITEM);
	$formitem="<OPTION VALUE=\"\">�A�C�e����I��";
	foreach my $idx (@itemlist)
		{
		$formitem.="<OPTION VALUE=\"$idx\">$ITEM[$idx]->{name}";
		}
	}
	eval {
	require "$INCLUDE_DIR/inc-version.cgi";
	};

	my($s,$min,$h,$d,$m,$y)=gmtime(time()+$TZ_JST);
	$y+=1900;$m++;

	$disp.="<hr width=700 noshade size=1><SPAN>��{�Ǘ��@�\\</SPAN>";
	$disp.="<table><tr><td bgcolor=\"#CBC5FF\"><table width=200>";
	$disp.="<tr><td>perl version</td><td>$]</td></tr>";
	foreach('.',$DATA_DIR,$INCLUDE_DIR,$AUTOLOAD_DIR,$TOWN_DIR,$COMMON_DIR,"_config.cgi","action.cgi",$MYNAME)
	{
		$disp.="<tr><td>".$_."<td>".substr(sprintf("%o",(stat($_))[2]),-3,3)."</tr>";
	}
	$disp.="</table><td bgcolor=\"#DBD5FF\">";
	
	$disp.=<<"HTML";
	<table width=500><tr><td colspan=2>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="menteon">
	<INPUT TYPE="SUBMIT" VALUE="�� �����e���[�h�Ɉڍs ��"></FORM>
	<td colspan=2><FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="menteoff">
	<INPUT TYPE="SUBMIT" VALUE="�� �����e���[�h������ ��">
	</FORM></tr><tr><td colspan=2>
	<FORM ACTION="admin.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="makeitem">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�� ���i�f�[�^���쐬 ��">
	</FORM>
	<td colspan=2><FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="item-list">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�� ���i�f�[�^���m�F ��">
	</FORM></tr><tr><td>
	<FORM TARGET="_blank" ACTION="http://www.geocities.co.jp/Playtown-Bingo/8587/diff/$BASE_VERSION.htm" METHOD="GET">
	<INPUT TYPE="SUBMIT" VALUE="�� �X�V���m�F ��">
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="treebbs">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�f����">
	</FORM>
	<td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="errdel">
	<INPUT TYPE="SUBMIT" VALUE="�G���[���폜">
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub2">
	<INPUT TYPE="HIDDEN" NAME=log VALUE=".">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�e�탍�O�{��">
	</FORM></tr><tr><td colspan=3>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub2">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�����o�[���X�g">
	<INPUT TYPE="CHECKBOX" NAME=host>�z�X�g�\\��
	<INPUT TYPE="CHECKBOX" NAME=only>�ꗗ�̂�
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="index.cgi" METHOD="POST">
	<INPUT TYPE="SUBMIT" VALUE="�g�b�v��ʂ�">
	</FORM></tr><tr><td colspan=4>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub2">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="delitem">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	�E�v���C�f�[�^���� <SELECT NAME=num1>$formitem</SELECT> �܂��� No.<INPUT TYPE=TEXT NAME=num2 SIZE=5> ��
	<INPUT TYPE="SUBMIT" VALUE="��������">
	</FORM></tr><tr><td colspan=4>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub2">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	�E�C�x���g�R�[�h <INPUT TYPE="TEXT" size=12 NAME=ecode> ��<br>
	�I������ <INPUT TYPE="TEXT" NAME=tlyear SIZE=5 VALUE="$y">�N<INPUT TYPE="TEXT" NAME=tlmon SIZE=3 VALUE="$m">��
	<INPUT TYPE="TEXT" NAME=tlday SIZE=3 VALUE="$d">�� <INPUT TYPE="TEXT" NAME=tlhour SIZE=3 VALUE="$h">��
	<INPUT TYPE="TEXT" NAME=tlmin SIZE=3 VALUE="$min">��<INPUT TYPE="TEXT" NAME=tlsec SIZE=3 VALUE="$s">�b
	�܂� <INPUT TYPE="SUBMIT" VALUE="����������">
	</FORM></tr></table>
	</tr></table><hr width=700 noshade size=1>
	<SPAN>�����o�[�ܕi���^�@�\\</SPAN>
	<table width=700 bgcolor="#DBD5FF"><tr><td>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�ܕi���^"> <SELECT NAME=user>$userselect</SELECT> 
	<INPUT TYPE="TEXT" size=46 NAME=comment VALUE="">���R�����g(�C��)<br>
	�E�A�C�e�� <SELECT NAME=senditem>$formitem</SELECT>�F<INPUT TYPE="TEXT" size=3 NAME=count VALUE="1">��
	�^�E�����F<INPUT TYPE="TEXT" size=5 NAME=sendmoney VALUE="0">�~
	�^�E���ԁF<INPUT TYPE="TEXT" size=3 NAME=sendtime VALUE="0">����
	�^�E�݈ʁF<INPUT TYPE="TEXT" size=3 NAME=senddig VALUE="0">�|�C���g<br>
	�����ꂼ�����x�Ɏw�肷�邱�Ƃ��ł��܂��B�R�����g���󗓂ɂ���ƌ��\\���܂���B
	</FORM></tr></table><hr width=700 noshade size=1>
	<SPAN>�����o�[�Ǘ��@�\\</SPAN>
	<table width=700 bgcolor="#DBD5FF"><tr><td width=280>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="new">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�V�K�X�܃I�[�v��"><br>
	������ɂ�����炸�I�[�v���\\�B</FORM>
	<td><FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="���[�U�[�X�ܓ��X"> <SELECT NAME=nm>$userselect</SELECT><br>
	���{�l�����X���Ă��Ă������ɑ���ł��܂��B
	</FORM></tr>
	<tr><td colspan=2>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="user">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE=HIDDEN NAME=mode VALUE=repass>
	<INPUT TYPE="SUBMIT" VALUE="�p�X���[�h�ύX"> <SELECT NAME=nm>$userselect</SELECT>
	<INPUT TYPE="TEXT" size=5 NAME=pw1 VALUE="">���V�p�X
	<INPUT TYPE="TEXT" size=5 NAME=pw2 VALUE="">���V�p�X������x
	</FORM></tr>
	<tr><td colspan=2>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="���[�U�[�X�ܓ���"> <SELECT NAME=user>$userselect</SELECT>
	<INPUT TYPE="TEXT"   NAME=blocklogin VALUE="">���������R<br>
	���uoff�v�Ɠ��͂œ��������F�umark�v�Ɠ��͂Ń��O�C���������O�F�ustop�v�Ɠ��͂ŋx�~����
	</FORM></tr>
	<tr><td colspan=2>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�d���o�^���^�֎~"> <SELECT NAME=user>$userselect</SELECT>
	<SELECT NAME=nocheckip><option value="nocheck">�d������<option value="check">�d���֎~</SELECT>
	</FORM></tr>
	<tr><td colspan=2>
	<FORM TARGET="_blank" ACTION="action.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=key VALUE="admin-sub">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="���[�U�[�X�ܒǕ�"> <SELECT NAME=user>$userselect</SELECT> 
	<INPUT TYPE="TEXT" NAME=comment VALUE="">���R�����g�i�C�Ӂj<br>
	<INPUT TYPE="CHECKBOX" NAME=log>���ʒm���Ȃ� 
	<INPUT TYPE="TEXT" NAME=closeshop VALUE="">�� �m�F�̂��� closeshop �Ɠ���
	</FORM></tr></table><hr width=700 noshade size=1>
	<SPAN>�f�[�^�������E�폜�@�\\</SPAN>
	<table width=700 bgcolor="#DBD5FF"><tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="init">
	<INPUT TYPE="SUBMIT" VALUE="������/�j���C��">�i�����@�\\�ł��B���łɂ���f�[�^�͍폜����܂���j
	</FORM></tr><tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	�Q�[���f�[�^�̂����C���i�f�[�^�E�֘A�f�B���N�g��������<INPUT TYPE="HIDDEN" NAME=mode VALUE="mini">
	<INPUT TYPE="SUBMIT" VALUE="�ŏ��A���C���X�g�[������"> <INPUT TYPE="PASSWORD" size=5 NAME=admin VALUE="">�Ǘ��p�X
	</FORM></tr>
	<tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	���[�U�[�f�[�^���c���C�Q�[���f�[�^�E�֘A�f�B���N�g����<INPUT TYPE="HIDDEN" NAME=mode VALUE="piece">
	<INPUT TYPE="SUBMIT" VALUE="�����A���C���X�g�[������"> <INPUT TYPE="PASSWORD" size=5 NAME=admin VALUE="">�Ǘ��p�X
	</FORM></tr>
	<tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	���[�U�[�f�[�^���܂߂āC�S�Q�[���f�[�^�E�֘A�f�B���N�g����<INPUT TYPE="HIDDEN" NAME=mode VALUE="delunit">
	<INPUT TYPE="SUBMIT" VALUE="���S�A���C���X�g�[������"> <INPUT TYPE="PASSWORD" size=5 NAME=admin VALUE="">�Ǘ��p�X
	</FORM></tr>
	<tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="timeedit">
	�ŏI�X�V������<INPUT TYPE="TEXT" NAME=tlyear SIZE=5 VALUE="$y">�N<INPUT TYPE="TEXT" NAME=tlmon SIZE=3 VALUE="$m">��
	<INPUT TYPE="TEXT" NAME=tlday SIZE=3 VALUE="$d">�� <INPUT TYPE="TEXT" NAME=tlhour SIZE=3 VALUE="$h">��
	<INPUT TYPE="TEXT" NAME=tlmin SIZE=3 VALUE="$min">��<INPUT TYPE="TEXT" NAME=tlsec SIZE=3 VALUE="$s">�b
	��<INPUT TYPE="SUBMIT" VALUE="�ύX����">
	<INPUT TYPE="PASSWORD" size=5 NAME=admin VALUE="">�Ǘ��p�X
	</FORM></tr>
	<tr><td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=mode VALUE="backup">
	�Q�[���f�[�^��<SELECT NAME=backup>$backupselect</SELECT>
	�̎��_��<INPUT TYPE="SUBMIT" VALUE="��������">
	<INPUT TYPE="PASSWORD" size=5 NAME=admin VALUE="">�Ǘ��p�X
	</FORM></tr></table><br><br>
HTML
1;
