# ���[�U�[���ύX���� 2005/03/30 �R��

Lock();
DataRead();
CheckUserPass();
$Q{er}='other';

my $functionname=$Q{mode};
OutError("bad request") if !defined(&$functionname);
&$functionname;

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

OutSkin();
1;


sub comment
{
	require $JCODE_FILE;
	$comment=jcode::sjis($Q{cmt},$CHAR_SHIFT_JIS&&'sjis');

	if(($comment) =~ /([,:;\t\r\n<>&])/
	|| CheckNGName($comment)
	)
		{
		OutError('�R�����g�Ɏg�p�ł��Ȃ��������܂܂�Ă��܂��B');
		}
	OutError('�R�����g�̕������������ł��B') if length($comment)>36;
	$comment=~s/&/&amp;/g;
	$comment=~s/>/&gt;/g;
	$comment=~s/</&lt;/g;
	$DT->{comment}=$comment;
	$disp.="�R�����g�X�V���܂���";
}

sub icon
{
	$DT->{icon}=$Q{icon};
	$disp.="�X���A�C�R���ύX���܂���";
}

sub shopname
{
	OutError('����������܂���B') if $DT->{money}<50000;
	require $JCODE_FILE;
	$Q{rename}=jcode::sjis($Q{rename},$CHAR_SHIFT_JIS&&'sjis');
	if(($Q{rename}) =~ /([,:;\t\r\n<>&])/
	|| CheckNGName($Q{rename})
	)
		{
		OutError('�X���Ɏg�p�ł��Ȃ��������܂܂�Ă��܂��B');
		}
	OutError('�X����20�����ȓ��ł��B') if length($Q{rename})>20;
	OutError('�X�����Z�����܂��B') if length($Q{rename})<4;
	OutError('���ɑ��݂���X���ł��B-> '.$Q{rename}) if GetDoubleName($Q{rename});;
	PushLog(1,0,$DT->{shopname}."���u".$Q{rename}."�v�ɓX�������߂܂����B");
	$DT->{shopname}=$Q{rename};
	$DT->{money}-=50000;
	$disp.=$DT->{shopname}."�։������܂����B<BR>�g�b�v�����X�������Ă��������B<BR><BR>";
	$disp.="<A HREF='index.cgi'>�g�b�v��</A>";
}

sub owname
{
	OutError('����������܂���B') if $DT->{money}<50000;
	require $JCODE_FILE;
	$Q{owname}=jcode::sjis($Q{owname},$CHAR_SHIFT_JIS&&'sjis');
	if(($Q{owname}) =~ /([,:;\t\r\n<>&])/
	|| CheckNGName($Q{owname})
	)
		{
		OutError('���O�Ɏg�p�ł��Ȃ��������܂܂�Ă��܂��B');
		}
	OutError('���O��12�����ȓ��ł��B') if length($Q{owname})>12;
	OutError('���O���Z�����܂��B') if length($Q{owname})<2;
	OutError('���ɑ��݂��閼�O�ł��B-> '.$Q{owname}) if $name2pass{$Q{owname}};
	PushLog(1,0,$DT->{name}."���u".$Q{owname}."�v�ɉ������܂����B");
	$DT->{name}=$Q{owname};
	$DT->{money}-=50000;
	$disp.=$DT->{name}."�։������܂����B<BR>�g�b�v�����X�������Ă��������B<BR><BR>";
	$disp.="<A HREF='index.cgi?u=$DT->{name}'>�g�b�v��</A>";
}

sub repass
{
	OutError('�m�F���͂ƕs��v�̂��ߕύX���~���܂��B') if $Q{pw1}ne$Q{pw2};
	OutError('�ύX�p�X���[�h�����͂���Ă��܂���B') if $Q{pw1}eq'';
	OutError('�p�X���[�h�Ɏg�p�ł��Ȃ�����������܂����̂ŕύX���~���܂��B') if $Q{pw1}=~/[^a-zA-Z0-9_\-]/;
	OutError('�p�X���[�h�� 8�����܂łł��B') if length($Q{pw1})>8;
	$DT->{pass}=$PASSWORD_CRYPT ? crypt($Q{pw1},GetSalt()) : $Q{pw1};
	$disp.="�p�X���[�h�ύX���܂���<BR>�g�b�v�����X�������Ă�������<BR><BR>";
	$disp.="<A HREF='index.cgi?nm=$DT->{name}&pw=$Q{pw1}'>�g�b�v��</A>";
}

sub restart
{
	OutError('�ďo���������ꍇ�� restart �Ɠ��͂��Ă��������B') if $Q{rss} ne 'restart';
	OutError('�n�ƌ�3���Ԉȓ��͍ďo���ł��܂���') if (($NOW_TIME-$DT->{foundation}) < 3600*3);

	my ($id,$name,$shopname,$pass,$icon)=($DT->{id},$DT->{name},$DT->{shopname},$DT->{pass},$DT->{icon});
	while(my($key,$val)=each %$DT) { delete $DT->{$key}; }
	($DT->{id},$DT->{name},$DT->{shopname},$DT->{pass},$DT->{icon},$DT->{time})=($id,$name,$shopname,$pass,$icon);
	$DT->{status}	      =1;
	$DT->{lastlogin}    =$NOW_TIME;
	$DT->{money}        =100000;
	$DT->{rank}         =5010;
	$DT->{foundation}   =$NOW_TIME;
	$DT->{showcasecount}=1;
	require "$ITEM_DIR/funcnew.cgi" if $DEFINE_FUNCNEW;
	opendir(SESS,$SUBDATA_DIR);
	my @dir=readdir(SESS);
	closedir(SESS);
	foreach(map{"$SUBDATA_DIR/$_"}grep(/^$DT->{id}\-.+\.cgi$/,@dir))
	{
		unlink $_;
	}
	PushLog(1,0,$DT->{shopname}."���C������V���ɏo�����܂����B");
	$disp.="�f�[�^������������܂����B<BR><BR>�C������V���ɂ���΂��Ă���������";
}

sub cls
{
	OutError('�X���܂��������ꍇ�� closeshop �Ɠ��͂��Ă��������B') if $Q{cls}ne'closeshop';
	SetCookieSession();
	$USERPASSURL=$USERPASSFORM="";
	CloseShop($DT->{id},'����X');
	PushLog(1,0,$DT->{shopname}."���X���܂����B");
	$disp.="�X���܂��̎葱���������������܂����B<BR><BR>"
		  ."�{�Q�[���ւ̎Q���C�{���ɂ��肪�Ƃ��������܂����B";
	$DTblockip=$DT->{remoteaddr};
}

sub guild
{
	OutError('�ޒc����ɂ�leave�Ɠ��͂��Ă�������') if $Q{guild} ne 'leave';
	OutError('�M���h�ɓ��c���Ă��Ȃ��̂őޒc�̕K�v������܂���') if !$DT->{guild};
	ReadGuild();
	my $name=$GUILD{$DT->{guild}}->[$GUILDIDX_name];
	$name="���U�����M���h" if $name eq '';;
	PushLog(1,0,$DT->{shopname}."���M���h�u".$name."�v����ޒc���܂����B");
	$disp.=$name."����ޒc���܂����B";
	delete $DT->{user}{_so_e};
	$DT->{guild}="";
}

