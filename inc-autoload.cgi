use utf8;
# プラグ認識 2003/07/19 由來

# 排他制御せず。

sub MakeIndexAutoLoad
{
	my($functionname)=@_;
	my $requirefile="";
	%autoload=();
	
	opendir(DIR,$AUTOLOAD_DIR);
	foreach my $file (sort(readdir(DIR)))
	{
		next if $file!~/\.cgi$/;
		
		open(IN,"<:encoding(UTF-8)","$AUTOLOAD_DIR/$file");
		while(<IN>)
		{
			next if !/^\s*sub\s+([^_]\w+)\s*$/;
			
			$requirefile="$AUTOLOAD_DIR/$file" if $1 eq $functionname;
			my $key=$1;
			$file=~/^([\w\-]+)\.cgi$/;
			$autoload{$key}=$1;
		}
	}
	closedir(DIR);
	
	open(OUT,">:encoding(UTF-8)",GetPath("autoload"));
	print OUT "\%autoload=qw(".join(" ",%autoload).");1;";
	close(OUT);
	
	require $requirefile if $requirefile ne '';
}
1;
