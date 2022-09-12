use utf8;
# ギルド編集フォーム 2004/01/20 由來

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
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>".l('ギルド受付')."</SPAN>：".l('こちらはギルド結成届出所です。')."<br>";
$disp.=l('ギルドを結成するには，$DIG_FORGUILDポイント以上の爵位が必要となります。').$TRE.$TBE."<br>";
$disp.=l("条件を満たしていません");
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
OutError(l('ギルドを変更できるのは団長だけです')) if (defined($id2idx{$leaderid}) && $leaderid != $DT->{id});
ReadLetterName();
$code=$DT->{guild};
$GUILD_DETAIL{$code}->{url}="http://" if !$GUILD_DETAIL{$code}->{url};
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>".l('ギルド受付')."</SPAN>：".l("こちらは").GetTagImgGuild($code);
$disp.=l("<BIG>%1</BIG> 執務室です。",$GUILD{$code}->[$GUILDIDX_name])."<br>";
$disp.=l("団長様，今後のギルドをどのようになさるおつもりですか？").$TRE.$TBE."<br>";
my $i=GuildCommonForm();

$disp.=<<"HTML";
<FORM ACTION="action.cgi" enctype="multipart/form-data" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="gd-b">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="edit">
$TB$TR$TDB<b>ギルドコード</b>
<td colspan=2><b>$code</b><INPUT TYPE=HIDDEN NAME=code VALUE="$code">$TRE
$TR$TDB<b>${\l('ギルド画像')}</b><br>(32*16pt)
<td colspan=2>${\l('gif形式画像のみ（指定しないと現状のまま）')}<br><input type=file name=upfile size=36>$TRE
$TR$TDB<b>${\l('ギルドホームページ')}</b><br>(${\l('60文字以内')})
<td colspan=2>${\l('一般向けホームページ')}<br><INPUT TYPE=TEXT NAME=url SIZE=56 VALUE="$GUILD_DETAIL{$code}->{url}">$TRE
$i
$TR$TDB<b>${\l('軍師任命')}</b><br>(${\l('各街 1名まで')})
HTML

my $r=int(scalar(@OtherDir) / 2 + 0.5);$r||=1;
foreach(0..$#OtherDir)
	{
	my $pg=$OtherDir[$_];
	$disp.=( ($_ % $r) ? "<br>" : $TD);
	$disp.="$Tname{$pg} <SELECT NAME=$pg><OPTION VALUE=\"\">".l('－－－－');
	foreach my $i(0..$Ncount{$pg})
		{
		$disp.="<OPTION VALUE=\"$LID{$pg}[$i]\"".($GUILD_DETAIL{$code}->{$pg}==$LID{$pg}[$i] ? ' SELECTED' : '').">$LNAME{$pg}[$i]";
		}
	$disp.="</SELECT>\n";
	}

$disp.=<<"HTML";
$TRE$TBE
<br><INPUT TYPE=SUBMIT VALUE="${\l('以上の内容で決定')}">
<br>(${\l('反映されるには数分かかります')})
</FORM>
HTML
}


sub GuildBuildMenu
{
$code="";
$disp.=$TB.$TR.$TD.$image[0].$TD."<SPAN>".l('ギルド受付')."</SPAN>：".l('こちらはギルド結成届出所です。')."<br>";
$disp.=l("新しい団長様，どのようなギルドを結成なさるおつもりですか？").$TRE.$TBE."<br>";
my $i=GuildCommonForm();

$disp.=<<"HTML";
<FORM ACTION="action.cgi" enctype="multipart/form-data" $METHOD>
<INPUT TYPE=hidden NAME=key VALUE="gd-b">
$USERPASSFORM
<INPUT TYPE=hidden NAME=mode VALUE="make">
$TB$TR$TDB<b>${\l('ギルドコード')}</b><br>(${\l('10文字以内')})
<td colspan=2>${\l('半角英数')}<b>${\l('小文字のみ')}</b><br><INPUT TYPE=TEXT NAME=code SIZE=10 VALUE="">$TRE
$TR$TDB<b>${\l('ギルド画像')}</b><br>(32*16pt)
<td colspan=2>${\l('gif形式画像のみ')}<br><input type=file name=upfile size=36>$TRE
$i
$TBE
<br><INPUT TYPE=SUBMIT VALUE="${\l('以上の内容で決定')}">
<br>(${\l('反映されるには数分かかります')})
</FORM>
HTML
}

sub GuildCommonForm
{
my $i.=<<"HTML";
$TR$TDB<b>${\l('ギルド正式名称')}</b><br>(${\l('%1文字以内',30)})
<td colspan=2>${\l('詳細表示の際に使われる名前')}<br><INPUT TYPE=TEXT NAME=name SIZE=24 VALUE="$GUILD_DETAIL{$code}->{name}">$TRE
$TR$TDB<b>${\l('ギルド通称')}</b><br>(${\l('%1文字以内',12)})
<td colspan=2>${\l('通常使われる名前')}<br><INPUT TYPE=TEXT NAME=shortname SIZE=12 VALUE="$GUILD_DETAIL{$code}->{shortname}">$TRE
$TR$TDB<b>${\l('ギルド間割引増率')}</b><br>(${\l('半角数字のみ')})
<td colspan=2>${\l('10倍の値を指定（30%にするには300と記入。10～500）')}<br><INPUT TYPE=TEXT NAME=dealrate SIZE=6 VALUE="$GUILD_DETAIL{$code}->{dealrate}">$TRE
$TR$TDB<b>${\l('ギルド間会費率')}</b><br>(${\l('半角数字のみ')})
<td colspan=2>${\l('10倍の値を指定（3%にするには30と記入。10～500）')}<br><INPUT TYPE=TEXT NAME=feerate SIZE=6 VALUE="$GUILD_DETAIL{$code}->{feerate}">$TRE
$TR$TDB<b>${\l('メンバー呼称')}</b><br>(${\l('%1文字以内',6)})
<td colspan=2>${\l('「会員」「同志」など')}<br><INPUT TYPE=TEXT NAME=member SIZE=6 VALUE="$GUILD_DETAIL{$code}->{member}">$TRE
$TR$TDB<b>${\l('決め台詞')}</b><br>(${\l('%1文字以内',30)})
<td colspan=2>${\l('一覧に表示される看板文句')}<br><INPUT TYPE=TEXT NAME=comment SIZE=24 VALUE="$GUILD_DETAIL{$code}->{comment}">$TRE
$TR$TDB<b>${\l('活動紹介')}</b><br>(${\l('%1文字以内',120)})
<td colspan=2>${\l('ギルドの活動目的や内容')}<br><INPUT TYPE=TEXT NAME=appeal SIZE=60 VALUE="$GUILD_DETAIL{$code}->{appeal}">$TRE
$TR$TDB<b>${\l('入団条件')}</b><br>(${\l('%1文字以内',120)})
<td colspan=2>${\l('「入りたい方は団長宛てに手紙を」など')}<br><INPUT TYPE=TEXT NAME=needed SIZE=60 VALUE="$GUILD_DETAIL{$code}->{needed}">$TRE
HTML
return $i;
}

