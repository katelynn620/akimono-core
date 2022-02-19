# ƒAƒCƒeƒ€”jŠü 2005/01/06 —R˜Ò

$NOMENU=1;
$Q{er}='stock';
Lock();
DataRead();
CheckUserPass();

$itemno=CheckItemNo($Q{item});
$itemname=$ITEM[$itemno]->{name};
$scale=$ITEM[$itemno]->{scale};
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$DT->{item}[$itemno-1]);

if ($ITEM[$itemno]->{flag}=~/h/) {

OutError('•s³‚È—v‹‚Å‚·') if ($ITEM[$itemno]->{flag}=~/t/);
OutError('‰ðŒÙl”‚ðŽw’è‚µ‚Ä‚­‚¾‚³‚¢') if !$count;

$ret=$itemname."‚ð".$count.$scale."‰ðŒÙ‚µ‚Ü‚µ‚½";
$disp.=$ret;
$DT->{item}[$itemno-1]-=$count;

 }	else	{

OutError('•s³‚È—v‹‚Å‚·') if ($ITEM[$itemno]->{flag}=~/t/);
OutError('”jŠü”—Ê‚ðŽw’è‚µ‚Ä‚­‚¾‚³‚¢') if !$count;

$ret=$itemname."‚ð".$count.$scale."ˆ•ª‚µ‚Ü‚µ‚½";
$disp.=$ret;
$DT->{item}[$itemno-1]-=$count;
$DT->{trush}+=int($ITEM[$itemno]->{price} * $count / 5);	#‚²‚Ý

$DTwholestore[$itemno-1]+=$count;
my $limit=0;
foreach $DT (@DT)
	{$limit+=$DT->{item}[$itemno-1];}

my $ITEM=$ITEM[$itemno];
my $limitcount=$ITEM->{wslimit}<0 ? -$ITEM->{wslimit} : int($ITEM->{wslimit}*($#DT+1));

if($limit+$DTwholestore[$itemno-1]>$limitcount)
{
	$limit=$limitcount if $limitcount<$limit;
	$DTwholestore[$itemno-1]=$limitcount-$limit;
}
$DTwholestore[$itemno-1]=0 if $DTwholestore[$itemno-1]<0;

	if ( $DT->{guild} && $ITEM[$itemno]->{price}) {
	ReadGuild();
	ReadGuildData();
	if ( $GUILD_DATA{$DT->{guild}}->{money} <= 0 ) {
		$disp.="<br>ƒMƒ‹ƒh‚©‚ç‚Ì•â•‹à‚Í‚ ‚è‚Ü‚¹‚ñ‚Å‚µ‚½";
		} else {
		my $guildmargin = int( $ITEM[$itemno]->{price} * $GUILD{$DT->{guild}}->[$GUILDIDX_dealrate] * $count / 1000 );
		$guildmargin = $GUILD_DATA{$DT->{guild}}->{money} if ($guildmargin > $GUILD_DATA{$DT->{guild}}->{money});
		$disp.="<br>ƒMƒ‹ƒh‚©‚ç".GetMoneyString($guildmargin)."‚Ì•â•‹à‚ªŽx‹‹‚³‚ê‚Ü‚µ‚½";
		$ret.="/ƒMƒ‹ƒh‚©‚ç".GetMoneyString($guildmargin)."Žx‹‹";
		EditGuildMoney($DT->{guild} ,-$guildmargin);
		$DT->{money}+=$guildmargin;
		WriteGuildData() ;
		}
	}
}

PushLog(0,$DT->{id},$ret);
RenewLog();
DataWrite();
DataCommitOrAbort();
UnLock();

OutSkin();
1;
