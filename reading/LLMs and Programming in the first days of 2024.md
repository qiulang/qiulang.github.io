# [LLMs and Programming in the first days of 2024](http://antirez.com/news/140)

[antirez](http://antirez.com/)

LLMs and Programming in the first days of 2024

I'll start by saying that this article is not meant to be a retrospective on LLMs. It's clear that 2023 was a special year for artificial intelligence: to reiterate that seems rather pointless. Instead, this post aims to be a testimony from an individual programmer. Since the advent of ChatGPT, and later by using LLMs that operate locally, I have made extensive use of this new technology. The goal is to accelerate my ability to write code, but that's not the only purpose. There's also the intent to not waste mental energy on aspects of programming that are not worth the effort. Countless hours spent searching for documentation on peculiar, intellectually uninteresting aspects; the efforts to learn an overly complicated API, often without good reason; writing immediately usable programs that I would discard after a few hours. These are all things I do not want to do, especially now, with Google having become a sea of spam in which to hunt for a few useful things.

Meanwhile, I am certainly not a novice in programming. I am capable of writing code without any aid, and indeed, I do so quite often. Over time, I have increasingly used LLMs to write high-level code, especially in Python, and much less so in C. What strikes me about my personal experience with LLMs is that I have learned precisely when to use them and when their use would only slow me down. I have also learned that LLMs are a bit like Wikipedia and all the video courses scattered on YouTube: they help those with the will, ability, and discipline, but they are of marginal benefit to those who have fallen behind. I fear that at least initially, they will only benefit those who already have an advantage.

But let's take it step by step.

## Omniscient or Parrots?

One of the most concerning phenomena of this new wave of novelty and progress in machine learning is the limited ability of AI experts to accept their limited knowledge. Homo sapiens invented neural networks, and then, even more crucially, an algorithm to automatically optimize the parameters of a neural network. Hardware has become capable of training increasingly larger models, and using statistical knowledge about the data to be processed (the priors) and through a lot of trial and error for successive approximations, architectures have been discovered that work better than others. But all in all, neural networks remain quite opaque.

In the face of this inability to explain certain emerging capabilities of LLMs, one would have expected more caution from scientists. Instead, many have deeply underestimated LLMs, saying that after all they were nothing more than somewhat advanced Markov chains, capable, at most, of regurgitating extremely limited variations of what they had seen in the training set. Then this notion of the parrot, in the face of evidence, was almost universally retracted.

At the same time, much of the enthusiastic masses attributed to LLMs supernatural powers that do not exist in reality. Unfortunately, LLMs can, at most, interpolate in the space represented by the data they have seen during training: and this would already be a lot. In reality, their ability to interpolate is limited (but still astonishing, and also unexpected). Oh, if only the largest LLMs of today could interpolate continuously in the space bounded by all the code they have seen! Even if they would not be able to produce true novelties, they would be able to replace 99% of programmers. The reality is more modest, as it almost always is. An LLM is certainly capable of writing programs that it has not seen in that exact form, showing a certain ability to blend different ideas that appeared in the training set with a certain frequency. It is also clear that this ability has, at the moment, deep limits, and whenever subtle reasoning is required, LLMs fail disastrously. Yet they represent the greatest achievement of AI, from its dawn to today. This seems undeniable.

## Stupid but All-Knowing

It's true: LLMs are capable, at most, of rudimentary reasoning, often inaccurate, many times peppered with hallucinations about non-existent facts. But they have a vast knowledge. In the field of programming, as well as in other fields for which quality data are available, LLMs are like stupid savants who know a lot of things. It would be terrible to do pair programming with such a partner (for me, pair programming is terrible even in the most general terms): they would have nonsensical ideas and we would have to continuously fight to impose our own. But if this erudite fool is at our disposal and answers all the questions asked of them, things change. Current LLMs will not take us beyond the paths of knowledge, but if we want to tackle a topic we do not know well, they can often lift us from our absolute ignorance to the point where we know enough to move forward on our own.

In the field of programming, perhaps their ability would have been of very little interest up to twenty or thirty years ago. Back then you had to know a couple of programming languages, the classic algorithms, and those ten fundamental libraries. The rest you had to add yourself, your own intelligence, expertise, design skills. If you had these ingredients you were an expert programmer, able to do more or less everything. Over time, we have witnessed an explosion of frameworks, programming languages, libraries of all kinds. An explosion of complexity often completely unnecessary and unjustified, but the truth is that things are what they are. And in such a context, an idiot who knows everything is a precious ally.

Let me give you an example: my experiments on machine learning were carried forward for at least a year using Keras. Then for various reasons, I switched to PyTorch. I already knew what an embedding or a residual network was, but I didn't feel like studying PyTorch's documentation step by step (as I had done with Keras, which I learned when ChatGPT did not yet exist). With LLMs, it was very easy to write Python code that used Torch. I just needed to have clear ideas about the model I wanted to put together and ask the right questions.

## Time for Examples

I'm not talking about easy things like: "Hey, what's the method of class X to do Y"? If it were just for that, one might be tempted to agree with those who are skeptical about LLMs. What the more complex models are capable of is much more elaborate. Until a few years ago, it would have been pure magic. I can tell GPT4: look, this is the neural network model I have implemented in PyTorch. These are my batches. I would like to resize the tensors so that the function that emits the batches is compatible with the input of the neural network, and I would like to represent things in this particular way. Can you show me the code needed to do the reshaping? GPT4 writes the code, and all I had to do was test in the Python CLI if the tensors really have the dimensions that are useful to me and if the data layout is correct.

Here's another example. Some time ago I had to implement a BLE client for certain ESP32-based devices. After some research, I realized that multi-platform Bluetooth programming bindings are more or less all unusable. The solution was simple, write the code in Objective C using macOS's native API. So, I found myself having to deal with two problems at the same time: learning the cumbersome BLE API of Objective C, full of patterns that I consider nonsensical (I'm a minimalist, that kind of API is at the opposite end of the spectrum of what I consider "good design") and at the same time remembering how to program in Objective C. The last time I had written a program in Objective C was ten years ago: I didn't remember the details of the event loop, memory management, and much more.

The final result is this code here, not exactly beautiful, but it does what it has to do. I wrote it in an extremely short time. It would have been impossible otherwise.

https://github.com/antirez/freakwan/blob/main/osx-bte-cli/SerialBTE.m

The code was written mostly by doing cut & paste on ChatGPT of the things I wanted to do and didn't quite know how to do, so they didn't work properly. Having the LLM explain to me what the problem was and how to solve it. It's true that the LLM didn't write much of that code, but it's also true that it significantly accelerated the writing. Would I have been able to do it without ChatGPT? Certainly yes, but the most interesting thing is not the fact that it would have taken me longer: the truth is that I wouldn't even have tried, because it wouldn't have been worth it. This fact is crucial. The ratio between the effort and the benefit of writing such a program, secondary to my project, would have been inconvenient. Moreover, this had a much more useful secondary collateral effect than the program itself: for that project I modified linenoise (one of my libraries for line editing) so that it works in multiplexing.

Another example, this time less about code writing and more about data interpretation. I wanted to set up a Python script using a convolutional neural network I found online, but it was quite lacking in documentation. The network had the advantage of being in ONNX format, so I could easily extract a list of inputs and outputs, and their assigned names. I only knew one thing about this convnet: it detected certain features within an image. I didn't know the input image format and size, and especially, the network's output was far more complicated than I imagined (I thought it was a binary classifier: is the observed image okay or does it have problems? Two outputs, but there were hundreds). I began by copy-pasting the ONNX network metadata output into ChatGPT. I explain to the assistant what little I know about the network. ChatGPT hypothesizes how the inputs are organized, and that the outputs are probably normalized boxes indicating parts of the images corresponding to potential defects, and other outputs indicating the likelihood of these defects. After a few minutes of back-and-forth, I had a Python script capable of network inference, plus the necessary code to transform the starting image into the tensor suitable for input, and so on. What struck me about that session was ChatGPT finally “understood” how the network functioned once it observed the raw output values (the logits, basically) on a test image: a series of floating-point numbers provided the context to identify the exact output details, the normalization, if the boxes where centred or if the left-top corner was specified, and so forth.

## Disposable Programs

I could document dozens of such cases I've narrated above. It would be pointless, as it's the same story repeating itself in more or less the same way. I have a problem, I need to quickly know something that *I can verify* if the LLM is feeding me nonsense. Well, in such cases, I use the LLM to speed up my need for knowledge.

However, there are different cases where I let the LLM write all the code. For example, whenever I need to write a more or less disposable program. Like this one:

https://github.com/antirez/simple-language-model/blob/main/plot.py

I needed to visualize the loss curve during the learning of a small neural network. I showed GPT4 the format of the CSV file produced by the PyTorch program during learning, and then I requested that if I specified multiple CSV files on the command line, I didn’t want the training and validation loss curves of the same experiment anymore, but a comparison of the validation loss curves of different experiments. The above is the result, as generated by GPT4. Thirty seconds in total.

Similarly, I needed a program that read the AirBnB CSV report and grouped my apartments by month and year. Then, considering the cleaning costs, and the number of nights per booking, it would do statistics on the average rental price for different months of the year. This program is extremely useful for me. At the same time, writing it is deadly boring: there's nothing interesting. So I took a nice piece of the CSV file and did copy-paste on GPT4. I wrote to the LLM what the problem was to be solved: the program worked on the first try. I show it to you in full below.

```python
import pandas as pd
pd.set_option('display.max_rows', None)
df = pd.read_csv('listings.csv')
reservations = df[df['Type'] == 'Reservation']
reservations['Start Date'] = pd.to_datetime(reservations['Start Date'])
reservations['Year'] = reservations['Start Date'].dt.year
reservations['Month'] = reservations['Start Date'].dt.month
reservations['Nightly Rate'] = (reservations['Amount'] - reservations['Cleaning Fee']) / reservations['Nights']
all_listings = reservations['Listing'].unique()
all_years = reservations['Year'].unique()
all_months = range(1, 13)
index = pd.MultiIndex.from_product([all_listings, all_years, all_months], names=['Listing', 'Year', 'Month'])
all_data = pd.DataFrame(index=index).reset_index()
merged_data = pd.merge(all_data, reservations, on=['Listing', 'Year', 'Month'], how='left')
average_nightly_rates = merged_data.groupby(['Listing', 'Year', 'Month'])['Nightly Rate'].mean().fillna(0)
print(average_nightly_rates)
```

To understand exactly how to group the data, which were otherwise quite scattered and disordered, requires some simple reasoning: it’s not a problem that an LLM could solve simply by regurgitating something that approximates the language it has seen. GPT4 has certainly observed similar programs during its training, but almost certainly has not seen a program that had to group things in the exact way I asked for and in a CSV file with that specific format. This shows (in my opinion) that LLMs can interpolate to some extent within the space outlined by the different programs in the training set.

Writing this type of program would be, in my opinion, an imprudent use of my time. The fact that an LLM can do it for me certainly speeds up my ability to produce code in a rather direct way: I can focus on the things that matter.

## When things don't go as they should: System Programming

Despite my success with LLMs and programming, when I write a program in C, I almost always end up using LLMs only as a more convenient form of documentation. I am an expert in system programming, and in that context, LLMs would be useful to me only if they were capable of complex reasoning: in this scenario, they almost always fail.

Let's start with the prompt of this experiment:

Outline the requirements of a nice, small but working C implementation of a bloom filter. Focus on the important aspects of the hashing function. Then write it, in good quality C.

Also consider that your example implementation should be sized to store 100,000 elements, with a false positive probability of at most 5%. The elements added are null-terminated strings.

Here’s the output:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define N 100000  // Number of elements
#define P 0.05    // False positive probability
#define M (int)(-(N * log(P)) / (log(2) * log(2)))  // Size of bit array
#define K (int)(M / N * log(2))  // Number of hash functions

unsigned char bitArray[M / 8 + 1];

void setBit(int n) {
    bitArray[n / 8] |= 1 << (n % 8);
}

int getBit(int n) {
    return bitArray[n / 8] & (1 << (n % 8));
}

// Basic hash functions (for demonstration purposes)
int hash1(char *str) {
    int hash = 5381;
    int c;
    while ((c = *str++))
        hash = ((hash << 5) + hash) + c;
    return abs(hash % M);
}

int hash2(char *str) {
    unsigned long hash = 0;
    int c;
    while ((c = *str++))
        hash = c + (hash << 6) + (hash << 16) - hash;
    return abs(hash % M);
}

void add(char *str) {
    setBit(hash1(str));
    setBit(hash2(str));
    // Add more hash functions if needed
}

int is_in(char *str) {
    return getBit(hash1(str)) && getBit(hash2(str));
    // Check more hash functions if used
}

int main() {
    char *testStr = "testString";
    add(testStr);

    if (is_in(testStr)) {
        printf("%s is probably in the set.\n", testStr);
    } else {
        printf("%s is definitely not in the set.\n", testStr);
    }

    return 0;
}
```

The implementation produced by GPT4 is not exactly brilliant. Bloom filters are quite widespread. It’s not such an exotic data structure. However, it’s clear that writing a decent bloom filter requires a greater capacity for abstraction: for example, there’s the problem of finding an effective way to hash the same string N times, and being certain that the hashes are sufficiently decorrelated.

Yet if you explicitly ask GPT4 to modify the hashing function so that it produces N decorrelated outputs, its proposed solution is significantly more acceptable:

```c
unsigned int hash(const char* str, unsigned int hash_id) {
    unsigned int hash = 5381;
    int c;
    while ((c = *str++)) {
        hash = ((hash << 5) + hash) + c + hash_id;
    }
    return hash % BF_SIZE;
}
```

If it had come up with this idea on its own, it would have written the bloom filter differently, setting K bits at a time using a single hashing function.

GPT4 was able to perform, in isolation, the task of writing an appropriate and more generic hashing function. But in the larger project of writing a bloom filter, it failed to show sufficient reasoning ability, and instead spat out two different but similar hashing functions: this is what one would expect from a poorly written article example on bloom filters.

The current weak reasoning abilities of Large Language Models, combined with a possible scarcity of sources on the subject, and even worse, potentially many low-quality sources, collectively result in this meager outcome. Yet, this is not an isolated case. The few times I attempt to use LLMs in the realm of algorithmic or system programming, the results are extremely poor, even when the expected reasoning abilities are not greater than what LLMs seem to possess in contexts like Python programming.

At the same time, GPT-4 is capable of decompiling the function it produced (in a separate session), and also precisely understand its purpose:

https://chat.openai.com/share/f54b64d7-d19a-4be4-8f10-08553aa812f1

Therefore, stating that there are no uses in system programming contexts is certainly inaccurate.

One interesting and pretty much expected thing is that, in these cases, the difference between smaller and larger models is indeed significant. Let’s see how two local models fare.

For instance, Mixtral, the MoE of Mistral, responded to the same question as follows:

```c
unsigned int hash(const char* str, unsigned int hash_id) {
    unsigned int hash = 5381;
    int c;
    while ((c = *str++)) {
        hash = ((hash << 5) + hash) + c;
    }
    return hash + hash_id;
}
```

Clearly, adding `hash_id` only at the end is an extremely poor solution. Mixtral is an excellent model for many uses, but as for the already weak reasoning capabilities of LLMs, the rule so far is certainly: larger is better.

This is a chat with the local **LLM deepseek-coder**, quantized to 4 bits as I don’t have enough RAM to use the model at higher precision. Yet, being 34 billion parameters large, its reasoning capabilities on this matter seem quite advanced. Here’s the log of the chat (conducted with llama.cpp):

> I have a hash function that should output N distinct hashes for the same data. However, I'm seeing a very poor distribution of the produced hashes as I change the value of hash_id:
>
> ```c
> unsigned int hash(const char* str, unsigned int hash_id) {
>     unsigned int hash = 5381;
>     int c;
>     while ((c = *str++)) {
>         hash = ((hash << 5) + hash) + c;
>     }
>     return hash + hash_id;
> }
> ```
>
> Maybe the salting strategy I'm using is poor? How could I change it?
>

[Deep-seek coder reply]

A possible issue with your implementation is that you're simply adding `hash_id` to the end of the hash. This can potentially lead to a poor distribution, especially if `hash_id` is too large or is not evenly distributed.

Consider using bitwise operations for mixing the `hash_id` in. Here is an example with XOR:

```c
unsigned int hash(const char* str, unsigned int hash_id) {
    unsigned int hash = 5381;
    int c;
    while ((c = *str++)) {
        hash = ((hash << 5) + hash) ^ c + hash_id; // Using XOR to mix in the hash_id
     }
    return (hash ^ hash_id); // Mixing the hash_id one more time at the end
}
```

This will spread `hash_id` throughout your hashes better than simply adding it, which can lead to less uniform distribution. [Snipped… the actual reply contained more informative stuff]

Not bad for a model running on my MacBook M1 Max. It also mixed the sums with XORs. In this case, the model was certainly helped by the fact that I provided clues about the problem to solve, but it was the model that identified what the real source of the trouble was, and the proposed alternative is valid. Something like the above is not within the reach of any book, documentation, or Google search. And as primitive, a result of interpolation, or however you want to perceive it, the model has performed some form of reasoning, if by reasoning, in this specific case, we accept the identification of the origin of a problem and its potential solution. However one wants to think about LLMs, stating that they are not helpful for programmers is extremely rash.

At the same time, however, my experience over the past few months suggests that for system programming, LLMs almost never provide acceptable solutions if you are already an experienced programmer. Let me show you another real world example. My current project, ggufflib, involves writing a library that reads and writes GGUF format files, which is the format in which llama.cpp loads quantized models. Initially, to understand how the quantization encodings worked (for speed reasons the bits of each quant are stored in fancy ways), I tried using ChatGPT, but then I resolved to reverse engineer llama.cpp's code: it was much faster. An LLM that can decently assist a system programmer, if it sees the data encoding “struct” declaration and the decoding function, should be able to reconstruct the data format documentation. The functions of llama.cpp were small enough to fit entirely in the context of GPT4, yet the output was completely useless. In these cases, things are done as in the past: paper and pen, reading the code, and seeing where the bits that the decoder extracts are registered.

Let me explain better the above use case so that you can try it yourself, if you wish. We have this structure from llama.cpp implementation.

```c
// 6-bit quantization
// weight is represented as x = a * q
// 16 blocks of 16 elements each
// Effectively 6.5625 bits per weight
typedef struct {
    uint8_t ql[QK_K/2];      // quants, lower 4 bits
    uint8_t qh[QK_K/4];      // quants, upper 2 bits
    int8_t  scales[QK_K/16]; // scales, quantized with 8 bits
    ggml_fp16_t d;           // super-block scale
} block_q6_K;
```

Then there is this function that is used to perform the dequantization:

```c
void dequantize_row_q6_K(const block_q6_K * restrict x, float * restrict y, int k) {
    assert(k % QK_K == 0);
    const int nb = k / QK_K;

    for (int i = 0; i < nb; i++) {
    
        const float d = GGML_FP16_TO_FP32(x[i].d);
        const uint8_t * restrict ql = x[i].ql;
        const uint8_t * restrict qh = x[i].qh;
        const int8_t  * restrict sc = x[i].scales;
        for (int n = 0; n < QK_K; n += 128) {
            for (int l = 0; l < 32; ++l) {
                int is = l/16;
                const int8_t q1 = (int8_t)((ql[l +  0] & 0xF) | (((qh[l] >> 0) & 3) << 4)) - 32;
                const int8_t q2 = (int8_t)((ql[l + 32] & 0xF) | (((qh[l] >> 2) & 3) << 4)) - 32;
                const int8_t q3 = (int8_t)((ql[l +  0]  >> 4) | (((qh[l] >> 4) & 3) << 4)) - 32;
                const int8_t q4 = (int8_t)((ql[l + 32]  >> 4) | (((qh[l] >> 6) & 3) << 4)) - 32;
                y[l +  0] = d * sc[is + 0] * q1;
                y[l + 32] = d * sc[is + 2] * q2;
                y[l + 64] = d * sc[is + 4] * q3;
                y[l + 96] = d * sc[is + 6] * q4;
            }
            y  += 128;
            ql += 64;
            qh += 32;
            sc += 8;
        }
    }
}
```

If I ask GPT4 to write an outline of the format used, it struggles to provide a clear explanation of how the blocks are stored on the lower / upper 4 bits of “ql” depending on the weight position. For this blog post, I also tried asking it to write a simpler function that shows how data is stored (maybe it can’t explain it with words, but can with code). The produced function is broken in many ways, the indexes are wrong, the 6-bit -> 8-bit sign extension is wrong (it just casts to uint8_t), and so forth.

Btw, this is the code that I ended writing myself:

    } else if (tensor->type == GGUF_TYPE_Q6_K) {
        uint8_t *block = (uint8_t*)tensor->weights_data;
        uint64_t i = 0; // i-th weight to dequantize.
        while(i < tensor->num_weights) {
            float super_scale = from_half(*((uint16_t*)(block+128+64+16)));
            uint8_t *L = block;
            uint8_t *H = block+128;
            int8_t *scales = (int8_t*)block+128+64;
            for (int cluster = 0; cluster < 2; cluster++) {
                for (uint64_t j = 0; j < 128; j++) {
                    f[i] = (super_scale * scales[j/16]) *
                           ((int8_t)
                            ((((L[j%64] >> (j/64*4)) & 0xF) |
                             (((H[j%32] >> (j/32*2)) & 3) << 4)))-32);
                    i++;
                    if (i == tensor->num_weights) return f;
                }
                L += 64;
                H += 32;
                scales += 8;
            }
            block += 128+64+16+2; // Go to the next block.
        }
   }

From the function above, I removed what was the actual contribution of this code: the long comments documenting the exact format used by llama.cpp Q6_K encoding. Now, it would be immensely useful if GPT could do this for me, and I bet it’s just a matter of months, because these kind of tasks are within what can be reached without any breakthrough, just with a bit of scaling.

## Putting Things in Perspective

I regret to say it, but it's true: most of today's programming consists of regurgitating the same things in slightly different forms. High levels of reasoning are not required. LLMs are quite good at doing this, although they remain strongly limited by the maximum size of their context. This should really make programmers think. Is it worth writing programs of this kind? Sure, you get paid, and quite handsomely, but if an LLM can do part of it, maybe it's not the best place to be in five or ten years.

And then, do LLMs have some reasoning abilities, or is it all a bluff? Perhaps at times, they seem to reason only because, as semioticians would say, the "signifier" gives the impression of a meaning that actually does not exist. Those who have worked enough with LLMs, while accepting their limits, know for sure that it cannot be so: their ability to blend what they have seen before goes well beyond randomly regurgitating words. As much as their training was mostly carried out during pre-training, in predicting the next token, this goal forces the model to create some form of abstract model. This model is weak, patchy, and imperfect, but it must exist if we observe what we observe. If our mathematical certainties are doubtful and the greatest experts are often on opposing positions, believing what one sees with their own eyes seems a wise approach.

Finally, what sense does it make today not to use LLMs for programming? Asking LLMs the right questions is a fundamental skill. The less it is practiced, the less one will be able to improve their work thanks to AI. And then, developing a descriptive ability of problems is also useful when talking to other human beings. LLMs are not the only ones who sometimes don't understand what we want to say. Communicating poorly is a great limitation, and many programmers communicate very poorly despite being very capable in their specific field. And now Google is unusable: using LLMs even just as a compressed form of documentation is a good idea. For my part, I will continue to make extensive use of them. I have never loved learning the details of an obscure communication protocol or the convoluted methods of a library written by someone who wants to show how good they are. It seems like "junk knowledge" to me. LLMs save me from all this more and more every day.