# �X�܏�� 2005/01/06 �R��

$disp.="<BIG>���X�܏��</BIG><br><br>";

my $tm=$NOW_TIME-$DT->{time};
if($tm<0)
{
	$tm=-$tm;
	$tm='�s���\�܂ł��� '.GetTime2HMS($tm);
}else{
	if($tm>$MAX_STOCK_TIME){$tm=$MAX_STOCK_TIME;}
	$tm=GetTime2HMS($tm);
}
my $rankmsg=GetRankMessage($DT->{rank});

my $expsum=0;
foreach(values(%{$DT->{exp}})){$expsum+=$_;}
$expsum=int($expsum/10)."%";

my $job="�����҂�";
$job=$JOBTYPE{$DT->{job}} if ($DT->{job});

my $level=DignityDefine($DT->{dignity},2);
$level=$DIGNITY[0] if !$level;

if(!$MOBILE)
{
	my @taxmode=('','(�Ɛ�)','(�{��)');
	$disp.=$TB;
	$disp.=$TR;
	$disp.="<td width=48 rowspan=2>".GetTagImgKao($DT->{name},$DT->{icon});
	$disp.="<td align=center colspan=4><SPAN>RANK ".($id2idx{$DT->{id}}+1)."</SPAN> �F ".GetTagImgGuild($DT->{guild})."<b>".$DT->{shopname}."</b>";
	$disp.="<td align=center rowspan=2>".GetTagImgJob($DT->{job},$DT->{icon}).$TRE;
	$disp.=$TR."<td width=56 class=b>�݈�$TD$level <small>(�o���l ".($DT->{dignity}+0)."pt)";
	$disp.=$TDB.'�W���u<td width=64>'.$job.$TRE;
	$disp.=$TR."<td colspan=2 class=b>�_��".$TD.$DT->{point}.$TDB."����";
	$disp.=$DT->{money}>=0 ? "<td colspan=2>".GetMoneyString($DT->{money}).$TRE : "<td colspan=2><font color=\"#cc2266\"><b>-".GetMoneyString(-$DT->{money})."</b></font>".$TRE;
	$disp.=$TR."<td colspan=2 class=b>��������".$TD.$tm.$TDB."�n��<td colspan=2>".GetTime2HMS($NOW_TIME-$DT->{foundation}).$TRE;
	$disp.=$TR."<td colspan=2 class=b>�l�C".$TD.$rankmsg.$TDB."����<td colspan=2>".GetCleanMessage($DT->{trush}).$TRE;
	$disp.=$TR."<td colspan=2 class=b>��������".$TD.GetMoneyString($DT->{saletoday}).$TDB."�O������<td colspan=2>\\".$DT->{saleyesterday}.$TRE;
	$disp.=$TR."<td colspan=2 class=b>�����x��".$TD.GetMoneyString($DT->{paytoday}).$TDB."�O���x��<td colspan=2>\\".$DT->{payyesterday}.$TRE;
	$disp.=$TR."<td colspan=2 class=b>�����ێ���<BR><SMALL>(���Z������)</SMALL>".$TD.GetMoneyString(int($DT->{costtoday}))."+".GetMoneyString($SHOWCASE_COST[$DT->{showcasecount}-1]);
	$disp.=   $TDB."�O���ێ���<td colspan=2>\\".$DT->{costyesterday}.$TRE;
	$disp.=$TR."<td colspan=2 class=b>�������p��".$TD.GetMoneyString($DT->{taxtoday}).$TDB."�O�����p��<td colspan=2>\\".($DT->{taxyesterday}+0).$TRE;
	$disp.=$TR."<td colspan=2 class=b>��{���p�ŗ�".$TD.GetUserTaxRate($DT,$DTTaxrate).'%'.$taxmode[$DT->{taxmode}+0].$TDB."�n���x���v<td colspan=2>".$expsum.$TRE;
	$disp.=$TR."<td colspan=2 class=b>�D����".$TD.($DT->{rankingcount}+0)."�� ".GetTopCountImage($DT->{rankingcount}+0).$TRE;
	$disp.=$GUILD{$DT->{guild}} ? $TDB."�M���h���<br><SMALL>(���Z������)</SMALL><td colspan=2>\\".int($DT->{saletoday}*$GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/1000)."<SMALL>/�����".($GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/10)."%</SMALL>" : $TD."�@<td colspan=2>�@";
	$disp.=$TRE.$TBE;
}
else
{
	$disp.="���O:".$DT->{name}."<BR>";
	$disp.="�X��:".GetTagImgGuild($DT->{guild}).$DT->{shopname}."<BR>";
	$disp.="RANK:".($id2idx{$DT->{id}}+1)."<BR>";
	$disp.="�l�C:".$rankmsg."<BR>";
	$disp.="����:".GetCleanMessage($DT->{trush})."<BR>";
	$disp.="����:".GetMoneyString($DT->{money})."<BR>";
	$disp.="����:".GetMoneyString($DT->{saletoday})."<BR>";
	$disp.="����:".GetMoneyString($DT->{paytoday})."<BR>";
	$disp.="����:".GetMoneyString(int($DT->{costtoday}))."+".GetMoneyString($SHOWCASE_COST[$DT->{showcasecount}-1])."<BR>";
	$disp.="����:".$tm."<BR>";
	$disp.="�_��:".$DT->{point}."<BR>";
	$disp.="�E��:".$job."<BR>";
}
1;
