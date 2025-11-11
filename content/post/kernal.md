---
title: "Spectre, pt 1"
date: 2025-11-07T18:50:23-04:00
draft: false
categories: []
tags: []
---

It's hard to overstate how much of an impact the Spectre and Meltdown vulnerabilities had on the way I think.
Hello. This will be a the first in a series of blog post about the ability.

```rust
if (x < array1.len())
    y = array2[array1[x] * 4096];
```