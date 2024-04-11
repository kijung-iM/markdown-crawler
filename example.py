from markdown_crawler import md_crawl
url = 'https://docs.whatap.io/java/introduction'
print(f'🕸️ Starting crawl of {url}')
md_crawl(
    url,
    max_depth=4,
    num_threads=5,
    base_dir='markdown',
    valid_paths=['/java'],
    target_content=['div.theme-doc-markdown.markdown'],
    is_domain_match=True,
    is_base_path_match=False,
    is_debug=True
)