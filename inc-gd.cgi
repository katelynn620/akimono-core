# �M���h������ 2004/02/28 �R��

ReadGuild();
ReadGuildData();

$image[0]=GetTagImgKao("�M���h��t","guild");
$disp.=GetMenuTag('gd','[�M���h�ꗗ]');
if (!$GUEST_USER && !$DT->{guild})
	{
	$disp.=GetMenuTag('gd-m','[���c�葱]');
	$disp.=GetMenuTag('gd-f','[�����錾]');
	$disp.='<hr width=500 noshade size=1>';
	}

if ($DT->{guild})
	{
	$disp.=GetMenuTag('gd-bbs','[��펺 '.GetTime2FormatTime((stat($COMMON_DIR.'/bbslog-'.$DT->{guild}.'.cgi'))[9]+0,1).']');
	$disp.=GetMenuTag('gd-i','[�T�㎺]','&cmd=info');
	if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id})
		{
		$disp.=GetMenuTag('gd-f','[������]');
		$disp.=GetMenuTag('gd-e','[�l����]','&mode=submit');
		$disp.=GetMenuTag('gd-m','[���c����]','&mode=submit');
		}
		else
		{
		if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id})
			{
			$disp.=GetMenuTag('gd-e','[�l����]','&mode=submit');
			$disp.=GetMenuTag('gd-m','[���c����]','&mode=submit');
			}
		$disp.=GetMenuTag('gd-e','[�ޒc�葱]','&mode=leave');
		}
	$disp.='<hr width=500 noshade size=1>';
	}
$disp.="<BIG>���M���h����</BIG><br><br>";
1;

