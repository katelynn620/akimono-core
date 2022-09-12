use utf8;
# ギルド一覧 2005/01/06 由來

DataRead();
CheckUserPass(1);
RequireFile('inc-gd.cgi');

if (!$DT->{guild})
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>${\l('ギルド受付')}</SPAN>：${\l('現在あるギルドの一覧です。')}<br>
${\l('クリックすると詳しい情報を見ることができます。')}
$TRE$TBE
HTML
GuildRanking();
}
elsif ($GUILD{$DT->{guild}}->[$GUILDIDX_name])
{
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>".l('ギルド受付')."</SPAN>：".l("こちらは").GetTagImgGuild($DT->{guild});
$disp.=l("<BIG>%1</BIG> 本部です。",$GUILD{$DT->{guild}}->[$GUILDIDX_name])."<br>";
$disp.=l("現在のギルドの情勢は，このようになっております。").$TRE.$TBE;
GuildRanking();
RequireFile('inc-guild-cmd.cgi');
}
else
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>${\l('ギルド受付')}</SPAN>：${\l('<b>%1</b>さんのギルドは，ただいま結成中です。',$DT->{shopname})}<br>
${\l('数分経ったら出来上がるはずですので，しばらくお待ちください。')}
$TRE$TBE
<br>※${\l('結成直後は，寄付などを行っても効果が現れないのでご注意ください。')}
HTML
}

OutSkin();
1;


sub GuildRanking
{
$disp.='<br>['.l('<BIG>ギルド対抗戦</BIG>終了まであと%1',GetTime2HMS($DTevent{guildbattle}-$DTlasttime)).']' if $DTevent{guildbattle};
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
	$disp.="<br><SPAN>".l('資金')."</SPAN> ".GetMoneyString($guild->{money});
	$disp.=l("(赤字)") if $guild->{money}<0;
	$disp.=qq|$TD<IMG class="i" SRC="$IMAGE_URL/guild-a$IMAGE_EXT">|.DefTarent($guild->{atk}+0);
	$disp.=qq|<br><IMG class="i" SRC="$IMAGE_URL/guild-b$IMAGE_EXT">|.DefTarent($guild->{def}+0);
	$disp.=$TD."<SPAN>".l('収入')."</SPAN> ".GetMoneyString($guild->{in});
	$disp.="<br><SPAN>".l('支出')."</SPAN> ".GetMoneyString($guild->{out});
	$disp.=$TD."<SPAN>".l('割引増率')."</SPAN> ".($dealrate/10)."%";
	$disp.="<br><SPAN>".l('会費率')."</SPAN> ".($feerate/10)."%".$TD;
	$disp.="<SPAN>".$member."</SPAN> ".($guildcount{$code}+0).l("名");
	if ($GUILD_DETAIL{$code}->{url})
		{$disp.=qq| <a target="_blank" href="action.cgi?key=jump&guild=$code">[${\l('HP')}]</a> |;}
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

