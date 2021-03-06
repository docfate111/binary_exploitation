#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/proc_fs.h>
#include <asm/uaccess.h>
#include <linux/slab.h>

#define NAME "hunter"

static long* ptr;

static ssize_t proc_write(struct file* file, const char* buf, size_t len, loff_t* off) {
	if (len != 9)
		return -EINVAL;
	char op = *buf;
	long v = *(long*)(buf+1);
	if (op == 's')
		ptr = (long*)v;
	else if (op == 'w')
		*ptr = v;
	else {
		printk(KERN_INFO "[x] invalid op (%c)\n", op);
		return -EINVAL;
	}
	return len;
}

static ssize_t proc_read(struct file* file, char* buf, size_t len, loff_t* off) {
	if (len != 8)
		return -EINVAL;
	if (!ptr) {
		char* heap = kmalloc(0x10, GFP_KERNEL);
		*(long*)buf = heap;
		printk(KERN_INFO "[+] have fun with your heap pointer :D %p\n", heap);
	}
	else
		*(long*)buf = *ptr;
	return len;
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
	printk(KERN_INFO "[+] hunter module loaded\n");
	return 0;
}

static void __exit m_exit(void) {
	remove_proc_entry(NAME, 0);
	printk(KERN_INFO "[+] hunter module unloaded\n");
}

MODULE_LICENSE("GPL");
module_init(m_init);
module_exit(m_exit);

