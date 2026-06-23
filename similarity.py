import hashlib

# SHINGLING
def get_shingles(doc,k=3):
    shingles=set()
    doc=doc.replace(" ", "").lower()
    
    for i in range(len(doc)-k+1):
        shingles.add(doc[i:i+k])
    return shingles


# HASH FUNCTION
def hash_func(x,seed):
    return int(hashlib.md5((x+str(seed)).encode()).hexdigest(),16)


# MINHASH
def get_minhash(shingles,num_hash=20):
    signature=[]
    
    for i in range(num_hash):
        min_val=float('inf')
        
        for sh in shingles:
            h=hash_func(sh,i)
            if h<min_val:
                min_val=h
    
        signature.append(min_val)
    
    return signature


# LSH (SIMPLE)
def lsh(sig1, sig2, bands=4, rows=5):
    for i in range(bands):
        band1=sig1[i*rows:(i+1)*rows]
        band2=sig2[i*rows:(i+1)*rows]
        
        if band1==band2:
            return True 
    
    return False


# JACCARD SIMILARITY
def jaccard(s1, s2):
    return len(s1&s2)/len(s1 | s2)


# MAIN
print("Document Similarity Checker")

doc1=input("Enter Document 1: ")
doc2=input("Enter Document 2: ")

# Step 1: Shingles
sh1 = get_shingles(doc1)
sh2 = get_shingles(doc2)

# Step 2: MinHash
sig1 = get_minhash(sh1)
sig2 = get_minhash(sh2)

# Step 3: LSH
is_similar = lsh(sig1, sig2)

# Step 4: Exact similarity
sim = jaccard(sh1, sh2)

print("\nJaccard Similarity:", round(sim, 2))

if is_similar:
    print("LSH Result: Documents are similar")
else:
    print("LSH Result: Documents are NOT similar")
