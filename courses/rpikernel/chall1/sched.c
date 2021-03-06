#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/proc_fs.h>
#include <asm/uaccess.h>
#include <linux/slab.h>

#define NAME "sched"

struct cpu_proc {
	struct cpu_proc* next;
	long prio;
	void (*compute)(void);
};

struct cpu_proc* head;

void high_prio(void) {printk(KERN_INFO "I'm kind of a big deal... People know me.\n");}
void med_prio(void) {printk(KERN_INFO "That's not my wallet...\n");}
void low_prio(void) {printk(KERN_INFO "We always find something, eh Didi, to give us the impression we exist?\n");}
void other_prio(void) {
	printk(KERN_INFO "What do we do now?\n");
	printk(KERN_INFO "Wait.\n");
	printk(KERN_INFO "Yes, but while waiting.\n");
	printk(KERN_INFO "What about hanging ourselves?\n");
	printk(KERN_INFO "Hmm. It'd give us an erection.\n");
}

struct cpu_proc* make_proc(long prio) {
	struct cpu_proc* pr = kmalloc(sizeof(struct cpu_proc), GFP_KERNEL);
	pr->next = NULL;
	pr->prio = prio;
	switch (prio) {
		case 0:
			pr->compute = high_prio;
			break;
		case 1:
			pr->compute = med_prio;
			break;
		case 2:
			pr->compute = low_prio;
			break;
		default:
			pr->compute = other_prio;
			break;
	}
	return pr;
}

void add_proc(struct cpu_proc* pr) {
	if (!head)
		head = pr;
	else {
		struct cpu_proc* tail = head;
		while (tail->next)
			tail = tail->next;
		tail->next = pr;
	}
}

struct cpu_proc* pop_proc(void) {
	struct cpu_proc* cur = head, *prev = NULL;
	struct cpu_proc* min = cur, *minPrev = prev;
	while (cur) {
		if (cur->prio < min->prio) {
			min = cur;
			minPrev = prev;
		}
		prev = cur;
		cur = cur->next;
	}
	if (!minPrev)
		head = min->next; //trigger null pointer when min is dereferenced
	else
		minPrev->next = min->next;
	return min;
}

static ssize_t proc_write(struct file* file, const char* buf, size_t len, loff_t* off) {
	long prio;
	if (sscanf(buf, "%ld", &prio) != 1) {
		printk(KERN_INFO "[x] expected long, not: %s\n", buf);
		return -EINVAL;
	}
	add_proc(make_proc(prio));
	printk(KERN_INFO "[+] added process with priority %ld\n", prio);
	return len;
}

static ssize_t proc_read(struct file* file, char* buf, size_t len, loff_t* off) {
	struct cpu_proc* pr = pop_proc();
	if (!pr)
		printk(KERN_INFO "[!] pls no hack me :P\n");
	else {
		pr->compute();
		printk(KERN_INFO "[+] ran process with priority: %ld\n", pr->prio);
	}
	return 0;
}

static const struct file_operations proc_ops = {
	.owner = THIS_MODULE,
	.write = proc_write,
	.read = proc_read
};

static int __init m_init(void) {
	struct proc_dir_entry* procfile = proc_create(NAME, 0666, 0, &proc_ops);
	if (!procfile) {
		printk(KERN_INFO "[!] couldnt create proc entry\n");
		return -ENOMEM;
	}
	printk(KERN_INFO "[+] scheduler module loaded\n");
	printk(KERN_INFO "[+] priority scheduling simulator\n");
	printk(KERN_INFO "[+] add process to queue with priority: echo '7' > /proc/sched\n");
	printk(KERN_INFO "[+] remove next process from queue: cat /proc/sched\n");
	add_proc(make_proc(1));
	add_proc(make_proc(0));
	add_proc(make_proc(2));
	add_proc(make_proc(51));
	printk(KERN_INFO "[+] sample processes queued\n");
	return 0;
}

static void __exit m_exit(void) {
	remove_proc_entry(NAME, 0);
	printk(KERN_INFO "[+] scheduler module unloaded\n");
	//what's a memory leak??
}

MODULE_LICENSE("GPL");
module_init(m_init);
module_exit(m_exit);

