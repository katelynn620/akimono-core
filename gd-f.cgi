# �M���h�ҏW�t�H�[�� 2004/01/20 �R��

$NOITEM=1;
DataRead();
CheckUserPass(1);
RequireFile('inc-gd.cgi');

if ($DT->{guild})
{
GuildEditMenu();
}
elsif ($DT->{dignity} < $DIG_FORGUILD)
{
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>�M���h��t</SPAN>�F������̓M���h�����͏o���ł��B<br>";
$disp.="�M���h����������ɂ́C$DIG_FORGUILD�|�C���g�ȏ�݈̎ʂ��K�v�ƂȂ�܂��B".$TRE.$TBE."<br>";
$disp.="�����𖞂����Ă��܂���";
}
else
{
GuildBuildMenu();
}
OutSkin();
1;


sub GuildEditMenu
{
my $leaderid=$GUILD_DETAIL{$DT->{guild}}->{leader};
OutError('�M���h��ύX�ł���̂͒c�������ł�') if (defined($id2idx{$leaderid}) && $leaderid != $DT->{id});
ReadLetterName();
$code=$DT->{guild};
$GUILD_DETAIL{$code}->{url}="http://" if !$GUILD_DETAIL{$code}->{url};
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>�M���h��t</SPAN>�F�������".GetTagImgGuild($code);
$disp.="<BIG>".$GUILD{$code}->[$GUILDIDX_name]."</BIG> �������ł��B<br>";
$disp.="�c���l�C����̃M���h���ǂ̂悤�ɂȂ��邨����ł����H".$TRE.$TBE."<br>";
my $i=GuildCommonForm();

$disp.=<<"HTML";
<FORM ACTION="action.cgi" enctype="multipart/form-data" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="gd-b">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="edit">
$TB$TR$TDB<b>�M���h�R�[�h</b>
<td colspan=2><b>$code</b><INPUT TYPE=HIDDEN NAME=code VALUE="$code">$TRE
$TR$TDB<b>�M���h�摜</b><br>(32*16pt)
<td colspan=2>gif�`���摜�̂݁i�w�肵�Ȃ��ƌ���̂܂܁j<br><input type=file name=upfile size=36>$TRE
$TR$TDB<b>�M���h�z�[���y�[�W</b><br>(60�����ȓ�)
<td colspan=2>��ʌ����z�[���y�[�W<br><INPUT TYPE=TEXT NAME=url SIZE=56 VALUE="$GUILD_DETAIL{$code}->{url}">$TRE
$i
$TR$TDB<b>�R�t�C��</b><br>(�e�X 1���܂�)
HTML

my $r=int(scalar(@OtherDir) / 2 + 0.5);$r||=1;
foreach(0..$#OtherDir)
	{
	my $pg=$OtherDir[$_];
	$disp.=( ($_ % $r) ? "<br>" : $TD);
	$disp.="$Tname{$pg} <SELECT NAME=$pg><OPTION VALUE=\"\">�|�|�|�|";
	foreach my $i(0..$Ncount{$pg})
		{
		$disp.="<OPTION VALUE=\"$LID{$pg}[$i]\"".($GUILD_DETAIL{$code}->{$pg}==$LID{$pg}[$i] ? ' SELECTED' : '').">$LNAME{$pg}[$i]";
		}
	$disp.="</SELECT>\n";
	}

$disp.=<<"HTML";
$TRE$TBE
<br><INPUT TYPE=SUBMIT VALUE="�ȏ�̓��e�Ō���">
<br>(���f�����ɂ͐���������܂�)
</FORM>
HTML
}


sub GuildBuildMenu
{
$code="";
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>�M���h��t</SPAN>�F������̓M���h�����͏o���ł��B<br>";
$disp.="�V�����c���l�C�ǂ̂悤�ȃM���h�������Ȃ��邨����ł����H".$TRE.$TBE."<br>";
my $i=GuildCommonForm();

$disp.=<<"HTML";
<FORM ACTION="action.cgi" enctype="multipart/form-data" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="gd-b">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="make">
$TB$TR$TDB<b>�M���h�R�[�h</b><br>(10�����ȓ�)
<td colspan=2>���p�p��<b>�������̂�</b><br><INPUT TYPE=TEXT NAME=code SIZE=10 VALUE="">$TRE
$TR$TDB<b>�M���h�摜</b><br>(32*16pt)
<td colspan=2>gif�`���摜�̂�<br><input type=file name=upfile size=36>$TRE
$i
$TBE
<br><INPUT TYPE=SUBMIT VALUE="�ȏ�̓��e�Ō���">
<br>(���f�����ɂ͐���������܂�)
</FORM>
HTML
}

sub GuildCommonForm
{
my $i.=<<"HTML";
$TR$TDB<b>�M���h��������</b><br>(30�����ȓ�)
<td colspan=2>�ڍו\\���̍ۂɎg���閼�O<br><INPUT TYPE=TEXT NAME=name SIZE=24 VALUE="$GUILD_DETAIL{$code}->{name}">$TRE
$TR$TDB<b>�M���h�ʏ�</b><br>(12�����ȓ�)
<td colspan=2>�ʏ�g���閼�O<br><INPUT TYPE=TEXT NAME=shortname SIZE=12 VALUE="$GUILD_DETAIL{$code}->{shortname}">$TRE
$TR$TDB<b>�M���h�Ԋ�������</b><br>(���p�����̂�)
<td colspan=2>10�{�̒l���w��i30%�ɂ���ɂ�300�ƋL���B10�`500�j<br><INPUT TYPE=TEXT NAME=dealrate SIZE=6 VALUE="$GUILD_DETAIL{$code}->{dealrate}">$TRE
$TR$TDB<b>�M���h�ԉ�</b><br>(���p�����̂�)
<td colspan=2>10�{�̒l���w��i3%�ɂ���ɂ�30�ƋL���B10�`500�j<br><INPUT TYPE=TEXT NAME=feerate SIZE=6 VALUE="$GUILD_DETAIL{$code}->{feerate}">$TRE
$TR$TDB<b>�����o�[�ď�</b><br>(6�����ȓ�)
<td colspan=2>�u����v�u���u�v�Ȃ�<br><INPUT TYPE=TEXT NAME=member SIZE=6 VALUE="$GUILD_DETAIL{$code}->{member}">$TRE
$TR$TDB<b>���ߑ䎌</b><br>(30�����ȓ�)
<td colspan=2>�ꗗ�ɕ\\�������Ŕ���<br><INPUT TYPE=TEXT NAME=comment SIZE=24 VALUE="$GUILD_DETAIL{$code}->{comment}">$TRE
$TR$TDB<b>�����Љ�</b><br>(120�����ȓ�)
<td colspan=2>�M���h�̊����ړI����e<br><INPUT TYPE=TEXT NAME=appeal SIZE=60 VALUE="$GUILD_DETAIL{$code}->{appeal}">$TRE
$TR$TDB<b>���c����</b><br>(120�����ȓ�)
<td colspan=2>�u���肽�����͒c�����ĂɎ莆���v�Ȃ�<br><INPUT TYPE=TEXT NAME=needed SIZE=60 VALUE="$GUILD_DETAIL{$code}->{needed}">$TRE
HTML
return $i;
}

