# �M���h�l�� 2004/01/20 �R��

Lock(), $Q{mode}=$Q{edit} if $Q{edit};
DataRead();
CheckUserPass();
RequireFile('inc-gd.cgi');

$Q{er}='gd';
my $functionname=$Q{mode};
$functionname||="leave";
OutError("bad request") if !defined(&$functionname);
&$functionname;

OutSkin();
1;


sub leave
{
OutError("bad request") if (!$DT->{guild});
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�M���h��t</SPAN>�F�M���h��ޒc���܂����H<br>
�����o�[�ɘA�����Ă���ޒc���邱�Ƃ��������߂��܂��B
$TRE$TBE<br>
HTML
$disp.="�M���h�풆�͑ޒc�ł��܂���",return if ($DTevent{guildbattle});
$disp.=<<STR;
	<form action="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="user">
	<INPUT TYPE=HIDDEN NAME=mode SIZE=10 VALUE="guild">
	$USERPASSFORM
	<SPAN>�M���h�ޒc</SPAN>
	<INPUT TYPE=TEXT NAME=guild SIZE=10 VALUE="">
	(leave�Ɠ���)
	<INPUT TYPE=SUBMIT VALUE="�ޒc����"></FORM>
STR
}

sub submit
{
OutError("bad request") if (!$DT->{guild});
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
OutError("bad request") if (!$ckeckok);
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�M���h��t</SPAN>�F�l�����ł́C�����o�[�Ɍ�������������C�ޒc��������ł��܂��B<br>
�������C���̊X�̃����o�[�Ɍ���܂��̂ł����ӂ��������B
$TRE$TBE<br>
HTML

my $formmember;
foreach(@DT)
{
	next if ($_->{guild} ne $DT->{guild});
	$formmember.="<OPTION VALUE=\"$_->{id}\">$_->{shopname}";
}

$disp.=<<STR;
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<BIG>������������</BIG>�F
<INPUT TYPE=HIDDEN NAME=edit VALUE="name">
<SELECT NAME=id SIZE=1>
<OPTION VALUE="">�I��
$formmember
</SELECT> �̌�������
<INPUT TYPE=TEXT NAME=name SIZE=16 VALUE="">
�� <INPUT TYPE=SUBMIT VALUE="��������"> (20�����ȓ�)
</FORM>
<hr width=500 noshade size=1>
<form action="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<SPAN>�ޒc����</SPAN>�F
<INPUT TYPE=HIDDEN NAME=edit VALUE="fire">
<SELECT NAME=id SIZE=1>
<OPTION VALUE="">�I��
$formmember
</SELECT> �� <INPUT TYPE=SUBMIT VALUE="�ޒc������">
<INPUT TYPE=TEXT NAME=guild SIZE=10 VALUE="">
(leave�Ɠ���)
</FORM>
STR
}

sub name
{
OutError("bad request") if (!$DT->{guild});
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
OutError("bad request") if (!$ckeckok);

OutError('�������鑊���I��ł��������B') if !$Q{id};
OutError('���݂��Ȃ��X�܂ł��B') if !defined($id2idx{$Q{id}});
my $tg=$id2idx{$Q{id}};
OutError('��������������܂���B') if ($DT[$tg]->{guild} ne $DT->{guild});
OutError('���������������ł��B') if length($Q{name})>20;

$DT[$tg]->{user}{_so_e}=$Q{name};
my $ret=$DT[$tg]->{shopname}."���u".$Q{name}."�v�ɏ����܂����B";
PushLog(2,0,"�M���h�u".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."�v��".$ret);
$disp.=$ret;

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
}

sub fire
{
OutError("bad request") if (!$DT->{guild});
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
OutError("bad request") if (!$ckeckok);

OutError('�ޒc�����郁���o�[��I��ł��������B') if !$Q{id};
OutError('���݂��Ȃ��X�܂ł��B') if !defined($id2idx{$Q{id}});
my $tg=$id2idx{$Q{id}};
OutError('����������܂���B') if ($DT[$tg]->{guild} ne $DT->{guild});
OutError('�c����ޒc�����邱�Ƃ͂ł��܂���B') if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $Q{id});
OutError('�ޒc������ɂ�leave�Ɠ��͂��Ă�������') if $Q{guild} ne 'leave';

delete $DT[$tg]->{user}{_so_e};
$DT[$tg]->{guild}="";
my $name=$GUILD{$DT->{guild}}->[$GUILDIDX_name];
PushLog(1,0,$DT[$tg]->{shopname}."���M���h�u".$name."�v���珜������܂����B");
$disp.=$DT[$tg]->{shopname}."��ޒc�����܂����B";

RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();
}

