use utf8;
# ギルド下請け 2004/02/28 由來

ReadGuild();
ReadGuildData();

$image[0]=GetTagImgKao(l("ギルド受付"),"guild");
$disp.=GetMenuTag('gd','['.l('ギルド一覧').']');
if (!$GUEST_USER && !$DT->{guild})
	{
	$disp.=GetMenuTag('gd-m','['.l('入団手続').']');
	$disp.=GetMenuTag('gd-f','['.l('結成宣言').']');
	$disp.='<hr width=500 noshade size=1>';
	}

if ($DT->{guild})
	{
	$disp.=GetMenuTag('gd-bbs','['.l('作戦室 '.GetTime2FormatTime((stat($COMMON_DIR.'/bbslog-'.$DT->{guild}.'.cgi'))[9]+0,1).'').']');
	$disp.=GetMenuTag('gd-i','['.l('探偵室').']','&cmd=info');
	if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id})
		{
		$disp.=GetMenuTag('gd-f','['.l('執務室').']');
		$disp.=GetMenuTag('gd-e','['.l('人事室').']','&mode=submit');
		$disp.=GetMenuTag('gd-m','['.l('入団許可').']','&mode=submit');
		}
		else
		{
		if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id})
			{
			$disp.=GetMenuTag('gd-e','['.l('人事室').']','&mode=submit');
			$disp.=GetMenuTag('gd-m','['.l('入団許可').']','&mode=submit');
			}
		$disp.=GetMenuTag('gd-e','['.l('退団手続').']','&mode=leave');
		}
	$disp.='<hr width=500 noshade size=1>';
	}
$disp.="<BIG>●".l('ギルド公館')."</BIG><br><br>";
1;

