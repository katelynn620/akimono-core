# URL�W�����v 2004/01/20 �R��

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
	$disp.="�M���h ".GetTagImgGuild($code).$guild->{name}."<br>";
	$disp.="<br>".$guild->{comment}."<br><br>";
	$disp.=GetTagA($guild->{name}."�֎����I�ɃW�����v���܂��B���Ȃ��ꍇ�͂��̃����N��H���Ă��������B",$guild->{url})."<br>";
	print "Refresh: 1; url=$guild->{url}\n";
}

sub JumpTown
{
	my($code)=@_;
	my $town=ReadTown($code);
	return if !$town || $town->{url} eq '';
	print "Refresh: 1; url=$town->{url}\n";
	$disp="";
	$disp.=GetTagA($town->{name}."�֎����I�ɃW�����v���܂��B���Ȃ��ꍇ�͂��̃����N��H���Ă��������B");
}


