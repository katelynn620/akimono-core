# �V�K�J�X 2004/01/20 �R��

$image[0]=GetTagImgKao("�ē��l","guide");
require $JCODE_FILE;
DataRead();

if($Q{admin} ne $MASTER_PASSWORD)
{
	OutError('�V�K�X�ܓo�^����������܂���B') if $NEW_SHOP_ADMIN;
	OutError('���Ȃ��͂��łɓX�܂������Ă��܂��B') if GetIPList(GetTrueIP());
	OutError('���Ȃ��͑��̊X�ł��łɓX�܂������Ă��܂��B') if $NEW_OTHERTOWN_BLOCK && GetDoubleIP(GetTrueIP());
	OutError('���Ȃ��͌��ݓo�^��������Ă��܂��B') if $NEW_SHOP_BLOCKIP && GetTrueIP() eq $DTblockip;
	OutError('�o�X�L�[���[�h������������܂���B') if $NEW_SHOP_KEYWORD && $Q{sname} && $Q{newkey} ne $NEW_SHOP_KEYWORD;
	checkMaxUser();
}

if($Q{sname}.$Q{name}.$Q{pass1}.$Q{pass2})
{
	$Q{name}=jcode::sjis($Q{name},$CHAR_SHIFT_JIS&&'sjis');
	$Q{sname}=jcode::sjis($Q{sname},$CHAR_SHIFT_JIS&&'sjis');

	if(($Q{sname}.$Q{name}.$Q{pass1}.$Q{pass2}) =~ /([,:;\t\r\n<>&])/
	|| ($Q{pass1}.$Q{pass2}) =~ /([^A-Za-z0-9_\-])/  #.$Q{name}���폜
	|| $Q{name} eq 'soldoutadmin'
	|| CheckNGName($Q{sname})
	|| CheckNGName($Q{name})  #���O�̃`�F�b�N��ǉ�
	)
	{
		OutError('���O�E�X���E�p�X���[�h�Ɏg�p�ł��Ȃ�'.
		         '�������܂܂�Ă��܂��B');
	}
	if(!$Q{sname} || !$Q{name} || !$Q{pass1} || !$Q{pass2})
	{
		OutError('���O�E�X���E�p�X���[�h����͂��Ă��������B');
	}
	if($Q{pass1} ne $Q{pass2})
	{
		OutError('�m�F�p�X���[�h������Ă��܂��B');
	}
	if(length($Q{sname})<4)
	{
		OutError('�X���̕����������Ȃ��ł��B');
	}
	if(length($Q{name})>12 || length($Q{sname})>20
	|| length($Q{pass1})>12 || length($Q{pass2})>8)
	{
		OutError('���O(�S�p6����)�E�X��(�S�p10����)�E�p�X���[�h(8����)�̕������������ł��B');
	}
	if( $Q{name} eq $Q{pass1} )
	{
		OutError('���O�ƃp�X���[�h�͓����ɂ��Ȃ��ł��������B');
	}
	
	Lock();
	DataRead();
	OutError('���ɑ��݂��閼�O�ł��B-> '.$Q{name}) if $name2pass{$Q{name}};
	OutError('���ɑ��݂���X���ł��B-> '.$Q{sname}) if GetDoubleName($Q{sname});;
	
	$idx=$DTusercount;
	$DTlasttime=$NOW_TIME if !$idx;
	$DT[$idx]={};
	$DT=$DT[$idx];
	$DT->{status}	    =1;
	$DT->{id}           =$DTnextid;
	$DT->{lastlogin}    =$NOW_TIME;
	$DT->{name}         =$Q{name};
	$DT->{shopname}     =$Q{sname};
	$DT->{icon}     =$Q{icon};
	$DT->{pass}         =$PASSWORD_CRYPT ? crypt($Q{pass1},GetSalt()) : $Q{pass1};
	$DT->{money}        =100000;
	$DT->{moneystock}   =0;
	$DT->{time}         =$NOW_TIME-12*60*60;
	$DT->{rank}         =5010;
	$DT->{saleyesterday}=0;
	$DT->{saletoday}    =0;
	$DT->{costtoday}    =0;
	$DT->{costyesterday}=0;
	$DT->{paytoday}     =0;
	$DT->{payyesterday} =0;
	$DT->{showcasecount}=1;
	$DT->{itemyesterday}={};
	$DT->{itemtoday}	={};
	$DT->{remoteaddr}   =GetTrueIP();
	$DT->{rankingyesterday}='';
	$DT->{taxtoday}     =0;
	$DT->{taxyesterday} =0;
	$DT->{foundation}   =$NOW_TIME;
	foreach $cnt (0..$DT->{showcasecount}-1)
	{
		$DT->{showcase}[$cnt]=0;
		$DT->{price}[$cnt]=0;
	}
	foreach $cnt (0..$MAX_ITEM-1)
	{
		$DT->{item}[$cnt]=0;
	}

	$DTblockip=$DT->{remoteaddr};

	require "$ITEM_DIR/funcnew.cgi" if $DEFINE_FUNCNEW;
	PushLog(1,0,$Q{sname}."���V���J�X���܂����B") if !$DEFINE_FUNCNEW || !$DEFINE_FUNCNEW_NOLOG;

	RenewLog();
	DataWrite();
	DataCommitOrAbort();
	UnLock();

	$disp=<<STR;
�X�ɐV�������X���a�����܂����B<br><br>
$TB$TR$TD
<SPAN>���O</SPAN>�F$Q{name}<BR>
<SPAN>�X��</SPAN>�F$Q{sname}<BR>
<SPAN>�p�X���[�h</SPAN>�F$Q{pass1}
$TRE$TBE
<BR>���p�X���[�h�͕K������������Ă����Ă��������B<BR><BR>
$TB$TR
$TD$image[0]$TD
�X�^�[�g������C�܂�<SPAN>[�f����]</SPAN>�ł�����������Ɨǂ��ł��傤�B<br>
�܂�<SPAN>[�}����]</SPAN>�Ɍo�c�̃q���g������܂��̂ň�ʂ育���������B
$TRE$TBE
<BR>
<A HREF=\"index.cgi?u=$Q{name}!$Q{pass1}\">�Q�[���X�^�[�g</A><BR><BR>
���O�C�����[��]��������BGM�����t���邱�Ƃ��ł��܂��B
STR
	OutSkin();
	exit;
}

RequireFile("inc-new.cgi");
OutSkin();
1;

sub checkMaxUser
{
	OutError($TB.$TR.$TD.$image[0].$TD.'�\���󂠂�܂��񂪁C���ݖ����ƂȂ��Ă���܂��B<BR>�󂫂��o��̂����҂����������B'.$TRE.$TBE)
		if $DTusercount>=$MAX_USER;
}

sub GetDoubleIP
{
	foreach my $pg(@OtherDir)
	{
	my $datafile='../'.$pg.'/data/user.cgi';
	my($ip)=@_;
	open(IN,$datafile) or return();
	my @data=<IN>;
	close(IN);
	my @list=map{(split(/\t/,$_))[4]}@data;
	@list=grep($_ eq $ip,@list) if $ip ne '';
	return @list if (@list);
	}
}
