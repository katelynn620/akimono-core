# d•¡“o˜^ŒŸo 2004/01/20 —R˜Ò

$NOMENU=1;
$Q{bk}="none";
$NOITEM=1;
DataRead();
CheckUserPass();
OutError("") if !$MASTER_USER;
$disp.="<BIG>œŠXŠÔ‚Ìd•¡“o˜^ó‹µ</BIG><br><br>";

@data=();
foreach my $i(@OtherDir) {
	$datafile='../'.$i.'/data/user.cgi';
	IpCheckOpen();
}
	my @list=map{(split(/\t/,$_))[4]}@data;
	$disp.='<table>';
	foreach $data(@data) {
		my($nm,$shop,$id,$tm,$ip,$agent,$ref)=split(/\t/,$data);
	my @check=grep($_ eq $ip,@list) if $ip ne '';
	$disp.='<tr><td>'.$shop.'<td>'.$tm.'<td>'.$ip.'<td><small>'.$agent.'</small><td>'.$ref."</tr>" if (@check)>1;
	}
	$disp.='</table>';

OutSkin();
1;


sub IpCheckOpen
{
	open(IN,$datafile) or return();
	my @temp=<IN>;
	push(@data, @temp);
	close(IN);
	return;
}

