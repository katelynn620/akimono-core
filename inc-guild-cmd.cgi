# �M���h�R�}���h 2005/01/06 �R��

my $usetime=3*60*60;
$disp.='<hr width=500 noshade size=1>';
GuildFundF();
$disp.='<hr width=500 noshade size=1>';
Break();
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
Force() if ($ckeckok);
1;

sub GuildFundF
{
	$stock=($DT->{money} - 100000);
	$disp.="<BIG>���M���h��t</BIG>�F �����̗]�T������܂���",return if ($stock < 100000);
$disp.=<<STR;
	<form action="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="gd-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=mode VALUE="fund">
	<BIG>���M���h��t</BIG>�F $term[0]
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	$msg{1000}=1000;
	$msg{10000}=10000;
	$msg{100000}=100000;
	$msg{1000000}=1000000;
	$msg{$stock}="$stock(�ő�z)";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1000,10000,100000,1000000,$stock))
	{
		last if $stock<$cnt || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
$disp.=<<STR;
	</SELECT>
	$term[1]�A�������� $term[0]
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2>$term[1]
	<INPUT TYPE=SUBMIT VALUE="��t����">
	</FORM>
STR
}

sub Break
{
	$disp.="<BIG>���M���h�u���C�N</BIG>�F �����������Ȃ��Ǝ��s�ł��܂���",return if (!$DT->{user}{_so_e});
	$disp.='<BIG>���M���h�u���C�N</BIG>�F ���Ԃ�����܂���',return if GetStockTime($DT->{time})<$usetime;
	$target="";
	foreach (keys(%GUILD))
	{
	$target.="<OPTION value=\"$_\">$GUILD{$_}->[$GUILDIDX_name]" if $GUILD_DATA{$_}->{money} > $GUILD_DATA{$DT->{guild}}->{money};
	}
	$disp.="<BIG>���M���h�u���C�N</BIG>�F ���肪���܂���",return if (!$target);
$disp.=<<STR;
<form action="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="gd-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="break">
<BIG>���M���h�u���C�N�F</BIG>
<SELECT NAME=tg>
<OPTION value="">
$target
</SELECT>
�ɑ΂���
<INPUT TYPE=SUBMIT VALUE="�U������">
STR
	$disp.="(�����:".GetTime2HMS($usetime).")</FORM>";
}

sub Force
{
	$disp.='<hr width=500 noshade size=1>';
	$disp.="<BIG>���R������</BIG>�F �����������Ȃ��Ǝ��s�ł��܂���",return if (!$DT->{user}{_so_e});
	$disp.='<BIG>���R������</BIG>�F ���Ԃ�����܂���',return if GetStockTime($DT->{time})<$usetime;
	$disp.="<BIG>���R������</BIG>�F �����̕K�v������܂���",return if ($GUILD_DATA{$DT->{guild}}->{atk} > 990);
$disp.=<<STR;
<form action="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="gd-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="force">
<BIG>���R�������F</BIG>
$GUILD{$DT->{guild}}->[$GUILDIDX_name]�̍U���͂�
<INPUT TYPE=SUBMIT VALUE="��������"> (�M���h����4����1����)
STR
	$disp.="(�����:".GetTime2HMS($usetime).")</FORM>";
}

