{
    "targets": [
        {
            "target_name": "uriparser2",
            "dependencies": [
                "libparsers"
            ],
            "sources": [
                "src/node-uriparser.cc"
            ],
            "include_dirs": [
                "<(module_root_dir)/build/ngx_url_parser/include/ngx_url_parser",
                "<(module_root_dir)/deps/ordered-map/",
                "<!(node -e \"require('nan')\")"

            ],
            "cflags": [
                "-O3"
            ],
            "libraries": [
                "<(module_root_dir)/build/ngx_url_parser/lib/libngx_url_parser.a",
            ]
        },
        {
            "target_name": "libparsers",
            "type": "none",
            "actions": [
                {
                    "action_name": "build",
                    "inputs": [""],
                    "outputs": [""],
                    "action": ["sh", "build_deps.sh"]
                }
            ]
        },
        {
            "target_name": "after_build",
            "type": "none",
            "dependencies": [
                "uriparser2"
            ],
            "actions": [
                {
                    "action_name": "copy",
                    "inputs": [
                        "<@(PRODUCT_DIR)/uriparser2.node"
                    ],
                    "outputs": [
                        "<(module_root_dir)/bin/uriparser2.node"
                    ],
                    "action": ["cp", "<@(PRODUCT_DIR)/uriparser2.node", "<(module_root_dir)/bin/uriparser2.node"]
                }
            ]
        }
    ]
}
