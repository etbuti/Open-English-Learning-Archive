# embeddb format notes

Status: Phase 1 / reverse engineering.

## Known observations

Sample: `NCE1A.EXE` extracted by Universal Extractor 2 produces a file named `embeddb`.

Observed markers:

- `ebookmm`
- `ebook mm file`
- `shinesoft ebookmm file system Plug-in`
- `binfiles[filename:S,bindata:B]`
- `realfiles[filename:S,offset:I,size:I]`
- `system.config[name:S,value:S]`
- `filelist.xml`
- lesson paths such as `1-5.htm`
- image paths such as `1-5.files/image001.jpg`
- one `.mp3` marker has been observed

## Working hypothesis

The file is not a standard ZIP/RAR/CAB container. It appears to be a proprietary MyEbook / ShineSoft resource database.

Likely table types:

```text
binfiles[filename:S,bindata:B]
realfiles[filename:S,offset:I,size:I]
```

Open questions:

1. exact table header layout
2. exact string encoding
3. whether payload blocks are compressed, encrypted, or offset-obfuscated
4. how `offset:I` and `size:I` are represented
5. whether media payloads are stored raw or protected
