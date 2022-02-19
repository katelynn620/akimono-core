# ƒMƒ‹ƒh‰º¿‚¯ 2004/02/28 —R˜Ò

ReadGuild();
ReadGuildData();

$image[0]=GetTagImgKao("ƒMƒ‹ƒhó•t","guild");
$disp.=GetMenuTag('gd','[ƒMƒ‹ƒhˆê——]');
if (!$GUEST_USER && !$DT->{guild})
	{
	$disp.=GetMenuTag('gd-m','[“ü’cè‘±]');
	$disp.=GetMenuTag('gd-f','[Œ‹¬éŒ¾]');
	$disp.='<hr width=500 noshade size=1>';
	}

if ($DT->{guild})
	{
	$disp.=GetMenuTag('gd-bbs','[ìíº '.GetTime2FormatTime((stat($COMMON_DIR.'/bbslog-'.$DT->{guild}.'.cgi'))[9]+0,1).']');
	$disp.=GetMenuTag('gd-i','[’T’ãº]','&cmd=info');
	if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id})
		{
		$disp.=GetMenuTag('gd-f','[·–±º]');
		$disp.=GetMenuTag('gd-e','[l–º]','&mode=submit');
		$disp.=GetMenuTag('gd-m','[“ü’c‹–‰Â]','&mode=submit');
		}
		else
		{
		if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id})
			{
			$disp.=GetMenuTag('gd-e','[l–º]','&mode=submit');
			$disp.=GetMenuTag('gd-m','[“ü’c‹–‰Â]','&mode=submit');
			}
		$disp.=GetMenuTag('gd-e','[‘Ş’cè‘±]','&mode=leave');
		}
	$disp.='<hr width=500 noshade size=1>';
	}
$disp.="<BIG>œƒMƒ‹ƒhŒöŠÙ</BIG><br><br>";
1;

