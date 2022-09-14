use utf8;
# URLジャンプ 2004/01/20 由來

$NOITEM=1;
$NOMENU=1;
JumpGuild($Q{guild}) if $Q{guild} ne '';
JumpTown($Q{town}) if $Q{town} ne '';
OutSkin();
exit;
1;

sub JumpGuild
{
	my($code)=@_;
	my $guild=ReadGuild($code);
	return if !$guild || $guild->{url} eq '';
	$disp="";
	$disp.=l("ギルド")." ".GetTagImgGuild($code).$guild->{name}."<br>";
	$disp.="<br>".$guild->{comment}."<br><br>";
	$disp.=GetTagA(l("%1へ自動的にジャンプします。しない場合はこのリンクを辿ってください。",$guild->{name}),$guild->{url})."<br>";
	print "Refresh: 1; url=$guild->{url}\n";
}

sub JumpTown
{
	my($code)=@_;
	my $town=ReadTown($code);
	return if !$town || $town->{url} eq '';
	print "Refresh: 1; url=$town->{url}\n";
	$disp="";
	$disp.=GetTagA(l("%1へ自動的にジャンプします。しない場合はこのリンクを辿ってください。",$town->{name}));
}


