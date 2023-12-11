# So let’s create a function called ft_tqdm.
# The function must copy the function tqdm with the yield operator.
# The fonction need to crate a progess bar with the percentage of the progression.
# Here’s how it should be prototyped:
# def ft_tqdm(lst: range) -> None:

def ft_tqdm(lst: range) -> None:
	"""
	Progress bar

	Parameters:
		lst (range): range of the progress bar
	Returns:
		None
		result:
			print a progress bar
	"""
	count = len(lst)
	size = 77
	def show(j):
			x = int(size*j/count)
			prefix = f"{j/count:.0%}"

			print(f"{prefix}|{u'█'*x}{(' '*(size-x))}| {j}/{count}", end='\r', flush=True)
	for i in lst:
		yield i
		show(i+1)
	print(flush=True)