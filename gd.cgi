# �M���h�ꗗ 2005/01/06 �R��

DataRead();
CheckUserPass(1);
RequireFile('inc-gd.cgi');

if (!$DT->{guild})
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�M���h��t</SPAN>�F���݂���M���h�̈ꗗ�ł��B<br>
�N���b�N����Əڂ����������邱�Ƃ��ł��܂��B
$TRE$TBE
HTML
GuildRanking();
}
elsif ($GUILD{$DT->{guild}}->[$GUILDIDX_name])
{
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>�M���h��t</SPAN>�F�������".GetTagImgGuild($DT->{guild});
$disp.="<BIG>".$GUILD{$DT->{guild}}->[$GUILDIDX_name]."</BIG> �{���ł��B<br>";
$disp.="���݂̃M���h�̏�́C���̂悤�ɂȂ��Ă���܂��B".$TRE.$TBE;
GuildRanking();
RequireFile('inc-guild-cmd.cgi');
}
else
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�M���h��t</SPAN>�F<b>$DT->{shopname}</b>����̃M���h�́C�������܌������ł��B<br>
�����o������o���オ��͂��ł��̂ŁC���΂炭���҂����������B
$TRE$TBE
<br>����������́C��t�Ȃǂ��s���Ă����ʂ�����Ȃ��̂ł����ӂ��������B
HTML
}

OutSkin();
1;


sub GuildRanking
{
$disp.='<br>[<BIG>�M���h�΍R��</BIG>�I���܂ł���'.GetTime2HMS($DTevent{guildbattle}-$DTlasttime).']' if $DTevent{guildbattle};
undef %guildcount;
foreach(@DT)
{
	$guildcount{$_->{guild}}++;
}
@guildlist=sort{$b->{money}<=>$a->{money}}map{$GUILD_DATA{$_}->{guild}=$_;$GUILD_DATA{$_}}keys(%GUILD);
my $Dguild=GetTownData('dominion');

my ($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar(@guildlist));

my $pagecontrol=GetPageControl($pageprev,$pagenext,"","",$pagemax,$page);
$disp.=$pagecontrol."<BR>";

my $rank=$pagestart+1;
my $writeflag=0;

$disp.=$TB;
foreach my $guild (@guildlist[$pagestart..$pageend])
{
	my $code    =$guild->{guild};
	$writeflag=1 , next if !$GUILD_DETAIL{$code};
	my $name    =$GUILD{$code}->[$GUILDIDX_name];
	my $dealrate=$GUILD{$code}->[$GUILDIDX_dealrate];
	my $feerate =$GUILD{$code}->[$GUILDIDX_feerate];
	my $comment =$GUILD_DETAIL{$code}->{comment};
	my $member =$GUILD_DETAIL{$code}->{member};
	
	$disp.=$TR;
	$disp.=$TDB."No.".$rank++."<td align=right>";
	$disp.="<A HREF=\"action.cgi?key=gd-o&$USERPASSURL&g=$code\">".GetTagImgGuild($code).$name."</a>";
	$disp.=qq|<IMG class="i" SRC="$IMAGE_URL/guildprize$IMAGE_EXT">| if ($code eq $Dguild);
	$disp.="<br><SPAN>����</SPAN> ".GetMoneyString($guild->{money});
	$disp.=    "(�Ԏ�)" if $guild->{money}<0;
	$disp.=qq|$TD<IMG class="i" SRC="$IMAGE_URL/guild-a$IMAGE_EXT">|.DefTarent($guild->{atk}+0);
	$disp.=qq|<br><IMG class="i" SRC="$IMAGE_URL/guild-b$IMAGE_EXT">|.DefTarent($guild->{def}+0);
	$disp.=$TD."<SPAN>����</SPAN> ".GetMoneyString($guild->{in});
	$disp.="<br><SPAN>�x�o</SPAN> ".GetMoneyString($guild->{out});
	$disp.=$TD."<SPAN>��������</SPAN> ".($dealrate/10)."%";
	$disp.="<br><SPAN>��</SPAN> ".($feerate/10)."%".$TD;
	$disp.="<SPAN>".$member."</SPAN> ".($guildcount{$code}+0)."��";
	if ($GUILD_DETAIL{$code}->{url})
		{$disp.=qq| <a target="_blank" href="action.cgi?key=jump&guild=$code">[HP]</a> |;}
	$disp.="<br>".$comment;
	$disp.=$TRE;
}
$disp.=$TBE;
$disp.=$pagecontrol;

if ($writeflag)
	{
	Lock();
	MakeGuildFile();
	WriteGuildData();
	DataWrite();
	RenewLog();
	DataCommitOrAbort();
	UnLock();
	}
}

sub DefTarent
{
	my($i)=@_;
	my $per=int($i/10);
	$per=100 if $per > 100;

	my $bar="";
	$bar ="<nobr>";
	$bar.=qq|<img src="$IMAGE_URL/b.gif" width="|.(    $per).qq|" height="12">| if $per;
	$bar.=qq|<img src="$IMAGE_URL/t.gif" width="|.(100-$per).qq|" height="12">| if $per!=100;
	$bar.="</nobr>";
	
	return $bar;
}

